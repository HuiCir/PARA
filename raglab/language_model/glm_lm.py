import os
import openai
import zhipuai
from zhipuai import ZhipuAI
import sys
import time
import logging
from tqdm import tqdm
from typing import Union, Tuple
import re
import numpy as np
from raglab.language_model.base_lm import BaseLM
import tiktoken
import pdb


class GLMModel(BaseLM):
    def __init__(self,args):
        super().__init__(args)
        self.generation_stop = args.generation_stop
        if self.generation_stop == '':
            self.generation_stop = None
        self.api_key_path = '/home/ps/Desktop/RAGLAB/api_keys.txt'
        self.client = self.load_model()

    def load_model(self):
        # load api key
        key_path = self.api_key_path
        assert os.path.exists(key_path), f"Please place your OpenAI APT Key in {key_path}."
        with open(key_path, 'r') as f:
            api_key = f.readline()
        client = ZhipuAI(api_key=api_key)
        return client

    def generate(self, inputs: Union[str,list[str]])-> list[BaseLM.Outputs]:
        '''
        Current version of OpenaiModel batch inference was not implemented
        '''
        if isinstance(inputs,str):
            inputs = [inputs]
        apioutputs_list = []
        for input_text in tqdm(inputs, desc="Generating outputs"):
            # original_text = input_text
            # input_text, is_modified = self.remove_sensitive_words(input_text)
            
            # if is_modified:
            #     logging.info(f"Remove sensitive text! origanl text: {original_text[:50]}... revised text: {input_text[:50]}...")
            
            message = [{"role": "user", "content": input_text}]

            response = self.call_GLM(message, model_name="glm-4-long", max_len=self.generate_maxlength, temp=self.temperature, top_p=self.top_p, stop = self.generation_stop)
            # collate Apioutputs
            apioutput = self.Outputs()
            if response is None:
                apioutput.text = 'None'
                apioutput.tokens_num = 0
                apioutputs_list.append(apioutput)
            else:
                apioutput.text = response.choices[0].message.content
                apioutput.tokens_ids = response.usage.total_tokens
                apioutput.prompt_tokens_num = response.usage.prompt_tokens
                apioutput.tokens_num = int(apioutput.tokens_ids)
                apioutputs_list.append(apioutput)
            print(apioutputs_list)
        return apioutputs_list



    
    def call_GLM(self,message, model_name="glm-4-long", max_len=1024, temp=0.7, top_p = 1.0, stop = None):
        # call GPT-3 API until result is provided and then return it
        response = None
        received = False
        num_rate_errors = 0


        while not received:
            try:
                response = self.client.chat.completions.create(
                                                        model=model_name,
                                                        temperature=temp,
                                                        top_p = top_p,
                                                        stop = stop,
                                                        messages=message)
                print(response)
                received = True
            except:
                num_rate_errors += 1
                error = sys.exc_info()[0]
                logging.critical(f"InvalidRequestError\nPrompt passed in:\n\n{message}\n\n")
                logging.error("API error: %s (%d). Waiting %dsec" % (error, num_rate_errors, np.power(2, num_rate_errors)))
                time.sleep(np.power(2, num_rate_errors))
                return None
        return response
