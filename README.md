# Probability Accumulation Retrieval-Augmented Generation with Active Selection

This repository is the implement for the paper Probability Accumulation Retrieval-Augmented Generation with Active Selection.

## Overview

Probability Accumulation Retrieval Augmentation (PARA). It emphasizes the reliable reintegration and utilization of retrieved information to enhance inferences of LLMs. Specifically, an information selection model, driven by LLMs' reasoning confidence, is proposed to replace the traditional retrieval-augmentation process. This enables the LLMs to actively select the most relevant retrieval results, thereby ensuring the quality of the retrieved content.

<p align="center">
  <img align="middle" src="fig/para.jpg" height="350" alt="PARA"/>
</p>

## Install environment
The code of PARA is implemented by RAGLAB. Please refer to the [RAGLAB repository](https://github.com/fate-ubw/RAGLab) for the complete conda environment configuration and retriever setting.


## Download Wikipedia knowledge database
Download the Wikipedia-23 base follow [the Document](https://github.com/fate-ubw/RAGLAB/blob/main/docs/process_wiki.md), and the first colbert processes embeddings may takes a long time.

## Setup Wikipedia search
Set up the colbert retriever using the following command:
```shell
cd RAGLAB
sh run/colbert_server/colbert_server_2023.sh
```

## Datasets
The experimental data were exclusively gathered from the same name open-source dataset, which is publicly accessible on GitHub or Hugging Face platforms, here are the list of the datasets.


- [PubHealth](https://huggingface.co/datasets/ImperialCollegeLondon/health_fact)
- [StrategyQA](https://huggingface.co/datasets/wics/strategy-qa)
- [PopQA](https://huggingface.co/datasets/akariasai/PopQA)
- [TriviaQA](https://huggingface.co/datasets/mandarjoshi/trivia_qa)
- [HotpotQA](https://huggingface.co/datasets/hotpotqa/hotpot_qa)
- [ASQA](https://huggingface.co/datasets/din0s/asqa)
If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. [RAGLAB repository](https://github.com/fate-ubw/RAGLab) have packaged all the data, so you just need to download it and it's ready to use.
  ~~~bash
  cd PARA
  huggingface-cli download PARA/data --local-dir data --repo-type dataset
  ~~~



### Models
```shell
cd PARA
mkdir model
cd model
mkdir output_models
# retriever model
mkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False

# llama3 generator
mkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
```

### Run PARA
Use the following command to run PARA with `dataset`. 
```shell
sh run/rag_inference/para/para-dataset-Llama3-baseline.sh 
```
