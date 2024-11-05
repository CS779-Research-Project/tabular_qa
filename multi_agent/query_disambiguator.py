## HF_TOKEN = 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

'''
------------------------------------------------
Query Disambiguator Notes : 
------------------------------------------------
Q : Is there a non-
'''

from datasets import load_dataset
import time
import outlines 
import torch
import pandas as pd
from typing import List
from pydantic import BaseModel, constr
from tqdm import tqdm

from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

LLM_NAME = "microsoft/Phi-3.5-mini-instruct"

dev_qa = pd.read_parquet("dev_qa.parquet")
train_qa = pd.read_parquet("train_qa.parquet")

list_one = dev_qa['dataset'].unique()
print(list_one)
print("_"*100)
list_two = train_qa['dataset'].unique()
print(list_two)
print("_"*100)

# merge the two lists
all_ds_ids = list(set(list_one).union(set(list_two)))
print(all_ds_ids)

ds_id = str('001_Forbes')
filtered_qa = train_qa[train_qa['dataset'] == ds_id]
df = pd.read_parquet(f"data/{ds_id}.parquet")