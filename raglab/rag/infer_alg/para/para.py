from typing import Optional, Any
from tqdm import tqdm
import pdb
import re
import spacy
from raglab.rag.infer_alg.naive_rag.naiverag import NaiveRag
from raglab.language_model import BaseLM

from typing import Optional
from tqdm import tqdm
import pdb
from raglab.rag.infer_alg.naive_rag.naiverag import NaiveRag

class para(NaiveRag):
    def __init__(self, args):
        super().__init__(args)
        self.init(args)
        self.ptheta = args.ptheta
        self.k = args.parak
        self.d = args.d


    def init(self,args):
        self.max_iteration = args.max_iteration
        self.nlp = spacy.load("en_core_web_sm")

    def infer(self, query: str, evidence)->tuple[str,dict[str,Any]]:
        '''
        infer function of naive rag
        '''
        generation_track = {}

        
        self.realtime_retrieval = True
        if self.realtime_retrieval:
            passages = self.retrieval.search(query) #self.retrieval.search(query) -> dict[int,dict]
            passages = self._truncate_passages(passages)
            collated_passages = self.collate_passages(passages)
            target_instruction = self.find_algorithm_instruction('Naive_rag-without_retrieval', self.task)
            input = target_instruction.format_map({'query': query})
            print(input)
            outputs_list = self.llm.generate(input) # llm.generate() -> list[BaseOutputs] so you have to get the text from BaseOutputs.text
            Outputs_o = outputs_list[0]
            probs_o = Outputs_o.tokens_prob
            oprob = self._out_prob(probs_o)
            #print(f'origin token prob:{oprob} \n')
            evi = self.chunk(query, collated_passages, oprob)
            self.print_fn(f"evidence: {evi}\n")
            target_instruction = self.find_algorithm_instruction('Naive_rag', self.task)
            input = target_instruction.format_map({'passages': evi, 'query': query})
            generation_track['cited passages'] = passages
            outputs_list = self.llm.generate(input)
            Outputs_e = outputs_list[0]
            probs_e = Outputs_e.tokens_prob
            eprob = self._out_prob(probs_e)
            print(f'evidence token prob:{eprob},  origin token prob:{oprob} \n')
        if Outputs_e.text == Outputs_o.text:
            outputs_text = Outputs_e.text
        else:
            if eprob > oprob:
                outputs_text = Outputs_e.text
            else:
                outputs_text = Outputs_o.text
        generation_track['final answer'] = outputs_text
        return outputs_text, generation_track
    
    def chunk(self,query, evidence, oprob ,t=3):
        evidence_passage = ""
        eprob = oprob
        Doc = self.nlp(evidence)
        sentlist = list(Doc.sents)
        print(len(sentlist))
        k = self.parak
        m = self.d
        for i in range(len(sentlist)):
            if k == 0 or eprob > self.ptheta:
                break
            if m + k > 0:
                relevant, eprob = self.detect(evidence_passage, sentlist[i].text, query, eprob)
                if relevant:
                    m = self.d
                    evidence_passage += sentlist[i].text
                    k -= 1
                else:
                    m -= 1
            else:
                continue

        print(f'evidence: {evidence_passage} \n')
        return evidence_passage

    def detect(self, evidence_passage, collated_passages, query, oprob):
        target_instruction = self.find_algorithm_instruction('Naive_rag', self.task)
        input = target_instruction.format_map({'passages': evidence_passage+collated_passages, 'query': query})
        outputs_list = self.llm.generate(input)
        Outputs_e = outputs_list[0]
        probs_e = Outputs_e.tokens_prob
        eprob = self._out_prob(probs_e)
        if eprob > oprob:
            print(f'DETECT: evidence token prob:{eprob},  origin token prob:{oprob} evidence text: {evidence_passage+collated_passages} \n')
            return True, eprob
        return False, oprob

    def _out_prob(self, group_list):
        if len(group_list) == 0:
            return 0
        group_prob = sum(group_list)/len(group_list)
        promax = group_list.index(min(group_list))
        return group_list[promax]