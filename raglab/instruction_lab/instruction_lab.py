ALGORITHM_INSTRUCTIONS = [
    {
        "algorithm_name": "-------------------Template-------------------------",
        "dataset_name": ""
    },
    {
        "algorithm_name": "Rules of naming:'-' seperate for naming. For example: Algorithm_name-mode-specific_stage",
        "dataset_name": "dataset name",
        "instruction": "Fill in your instruction here"
    },
    {
        "algorithm_name": "-------------------Naive Rag-------------------------",
        "dataset_name": ""
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "",
        "instruction": "### Instruction:\n Now, based on the following passages and your knowledge, please answer the question more succinctly and professionally. ### Background Knowledge:\n {passages} \n\n## Input:\n\n{query}\n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "PopQA",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge, please answer the question more succinctly and professionally. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "PopQA-posterior_instruction",
        "instruction": "### Instruction:\n Now, based on the passages and your internal knowledge, please answer the question more succinctly and professionally. ### Retrieved Knowledge:\n {passages}\n \n## Input:\n\n{query}\n\n ### Response:\n"
    }, 
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "PopQA",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "TriviaQA",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge, please answer the question more succinctly and professionally. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "TriviaQA",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "StrategyQA",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge. You are only allowed to answer True or False, and generating other types of responses is prohibited. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "StrategyQA",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n You are only allowed to answer True or False, and generating other types of responses is prohibited. ### Response:\n"
    },{
        "algorithm_name": "Naive_rag",
        "dataset_name": "AVeriTeC",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge, please answer the question more succinctly and professionally. You are only allowed to answer Supported or Refuted, and generating other types of responses is prohibited. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "AVeriTeC",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n You are only allowed to answer Supported or Refuted, and generating other types of responses is prohibited. ### Response:\n"
    },{
        "algorithm_name": "Naive_rag",
        "dataset_name": "Fever2",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge. You are only allowed to answer SUPPORTS or REFUTES, and generating other types of responses is prohibited. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "Fever2",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n You are only allowed to answer SUPPORTS or REFUTES, and generating other types of responses is prohibited. ### Response:\n"
    },{
        "algorithm_name": "Naive_rag",
        "dataset_name": "Hover",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge. You are only allowed to answer SUPPORTED or REFUTED, and generating other types of responses is prohibited. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "Hover",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n You are only allowed to answer SUPPORTED or REFUTED, and generating other types of responses is prohibited. ### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "HotPotQA",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge, please answer the question more succinctly and professionally. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "HotPotQA",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "2WikiMultiHopQA",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge, please answer the question more succinctly and professionally. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "2WikiMultiHopQA",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "MMLU",
        "instruction": "### Instruction:\n Given four answer candidates, A, B, C and D, choose the best answer choice. \n## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge, please answer the question more succinctly and professionally. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "MMLU",
        "instruction": "### Instruction:\n Given four answer candidates, A, B, C and D, choose the best answer choice. \n## Input:\n\n{query}\n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "Arc",
        "instruction": "### Instruction:\nGiven four answer candidates, A, B, C and D, choose the best answer choice.\n\n## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge, please answer the question more succinctly and professionally. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "Arc-posterior_instruction",
        "instruction": "### Instruction:\nNow, based on the passages and your internal knowledge, please answer the question more succinctly and professionally. ### Retrieved Knowledge:\n {passages}\n  Given four answer candidates, A, B, C and D, choose the best answer choice.\n\n## Input:\n\n{query}\n\n  ### Response:\n"
    }, 
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "Arc",
        "instruction": "### Instruction:\nGiven four answer candidates, A, B, C and D, choose the best answer choice.\n\n## Input:\n\n{query}\n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "PubHealth",
        "instruction": "### Instruction:\nIs the following statement correct or not? You are only allowed to answer True or False, and generating other types of responses is prohibited\n\n## Input:\n\n{query}\n\n Determine the statement based on the following passages and your knowledge ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "PubHealth-posterior_instruction",
        "instruction": "### Instruction\nDetermine the statement based on the passages and your internal knowledge. ### Retrieved Knowledge:\n {passages}\n  Is the following statement correct or not? Say true if it's correct; otherwise say false\n\n## Input:\n\n{query}\n\n  n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "PubHealth",
        "instruction": "### Instruction:\nDetermine the statement based on the passages and your internal knowledge. Say true if it's correct; otherwise say false\n\n## Input:\n\n{query}\n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "ASQA",
        "instruction": "### Instruction:\nAnswer the following question. The question may be ambiguous and have multiple correct answers, and in that case, you have to provide a long-form answer including all correct answers.## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge, please answer the question more succinctly and professionally. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "ASQA",
        "instruction": "### Instruction:\nAnswer the following question. The question may be ambiguous and have multiple correct answers, and in that case, you have to provide a long-form answer including all correct answers.## Input:\n\n{query}\n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "Factscore",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n Now, based on the following passages and your knowledge, please answer the question more succinctly and professionally. ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "Factscore",
        "instruction": "### Instruction:\n## Input:\n\n{query}\n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag",
        "dataset_name": "Feverous",
        "instruction": "### Instruction:\n Determine if there is Observation that SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFORMATION. You can only answer SUPPORTS, REFUTES, or NOT ENOUGH INFORMATION, and you are prohibited from generating other responses, and the answers generated must be all in capital letters. \n## Input:\n\n{query}\n\n Determine the claim based on the following passages and your knowledge ### Background Knowledge:\n {passages} \n\n### Response:\n"
    },
    {
        "algorithm_name": "Naive_rag-without_retrieval",
        "dataset_name": "Feverous",
        "instruction": "### Instruction:\n Determine if there is Observation that SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFORMATION. You can only answer SUPPORTS, REFUTES, or NOT ENOUGH INFORMATION, and you are prohibited from generating other responses, and the answers generated must be all in capital letters. \n## Input:\n\n{query}\n\n### Response:\n"
    }
]