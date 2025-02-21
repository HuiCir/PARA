from raglab.rag.infer_alg.naive_rag import NaiveRag
from raglab.rag.infer_alg.para import para

ALGOROTHM_LIST = ['naive_rag', 'para']
def get_algorithm(args):
    if args.algorithm_name == 'naive_rag':
        Rag = NaiveRag(args) 
    elif args.algorithm_name == 'para':
        Rag = para(args)
    else:
        raise AlgorithmNotFoundError("Algorithm not recognized. Please provide a valid algorithm name.")
    return Rag

class AlgorithmNotFoundError(Exception):
    pass