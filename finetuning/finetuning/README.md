# LLM Lora fine-tuning example Sentiment Analysis

An example to show how to finetune an LLM with Lora using Azure ML. This particular example fine-tunes an LLM to improve sentiment analysis of a dataset stored in all-data.csv.

Step 1: `cd llm`

Step 2: update azure-ml-job.yaml to specify the compute target in your workspace. You need to create a compute or cluster in azure ml for this.

Step 3: Run the job 
`az ml job create -f ./src/finetuning/azure-ml-job.yaml --resource-group RG_NAME --workspace-name WS_NAME`

When the image is built, the job takes about 8-11 mins to run. The finetuning only takes a couple of minutes on the small dataset.

You can specify a different model using the model_name parameter in the azure-ml-job.yaml file. For example, a smaller model is: `"microsoft/phi-2"`. You can find these names from Huggingface model cards.

FYI: The code in the main.py file is based on this: https://www.kaggle.com/code/simranjeetsingh1430/microsoft-phi2-llm-fine-tuning-qlora

## Multi-GPU Training

In ./src/finetuning you can run the acclerate commands to parallelise training across multi-gpus on a multi-gpu machine

`az ml job create -f ./src/finetuning/azure-ml-job-multigpu.yaml --resource-group RG_NAME --workspace-name WS_NAME`


The azure-ml-job.yaml file contains the command to execute the main.py file:

The model name comes from Huggingface model cards.

`python main.py --model_name "Intel/neural-chat-7b-v3-3" --filename "./all-data.csv" `

A smaller model is: `"microsoft/phi-2"`

If the model is too big for the GPU then you can use 8bit or 4bit quantisation like this:


`python main.py --model_name "" --filename "./all-data.csv" --use_8bit=True`

`python main.py --model_name "" --filename "./all-data.csv" --use_4bit=True`

## Running locally

There is a docker image and requirements.txt file in ./src/finetuning/environment

You can use the following command to build the docker image and run it as a terminal:

Run the following:


```
cd llm

./make terminal exp=finetuning run-xargs="--gpus all"
```

## Loading a Lora fine-tuned model

In ./src/finetuning/finetuning_inference.ipynb there is code to show how to load a base model and a Lora fine-tuned model and how to call them using huggingface and langchain. 

The pip requirements are contained in the ./src/finetuning/environment folder.


## Data

There are two datasets. Both from Kaggle.

Reddit data:

The following webpage shows doing the sentiment analysis on OpenAI GPT 3.5 and finetuning on the same.
https://wandb.ai/mostafaibrahim17/ml-articles/reports/Fine-Tuning-ChatGPT-for-Sentiment-Analysis-With-W-B--Vmlldzo1NjMzMjQx

Results on GPT 3.5: 48% then 73% after fine-tuning (only 100 rows though!)

I only got 66% after fine-tuning. But I suspect the GPT result was testing on the training set.


Finance data:

https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news/data

This works a lot better, I'm getting 85% on Intel Neuralchat. The base model appears to be a significant influence on which results are best. 
