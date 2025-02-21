from raglab.dataset.PopQA import  PopQA
from raglab.dataset.PubHealth import PubHealth
from dataclasses import dataclass

class AVeriTeC(PubHealth):
    def __init__(self, args):
        super().__init__(args)

    @dataclass
    class InputStruction:
        question:str =  'claim'
        answer:str = 'label'
        pregiven_passages = 'justification'

    @dataclass
    class OutputStruction:
        question:str = 'question'
        answer:str = 'answer' 
        generation:str = 'generation'