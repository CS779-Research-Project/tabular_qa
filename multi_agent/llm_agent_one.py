## Import necessary libraries
from datasets import load_dataset
import time
import outlines 
import torch
import pandas as pd
from typing import List
from pydantic import BaseModel, constr
from tqdm import tqdm
import os
import argparse

from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Argument parser to allow passing LLM_NAME and OUT_FOLDER as arguments
parser = argparse.ArgumentParser(description="Run question breakdown with LLM.")
parser.add_argument('--llm_name', type=str, required=True, help='Name of the language model to be used')
parser.add_argument('--out_folder', type=str, required=True, help='Folder where the output files will be saved')
args = parser.parse_args()

LLM_NAME = args.llm_name
OUT_FOLDER = args.out_folder

# If the output folder does not exist, create it
if not os.path.exists(OUT_FOLDER):
    os.makedirs(OUT_FOLDER)

# Load datasets
dev_qa = pd.read_parquet("dev_qa.parquet")
train_qa = pd.read_parquet("train_qa.parquet")

# merge dev_qa into train_qa
train_qa = pd.concat([train_qa, dev_qa])

# Get unique dataset ids
list_one = dev_qa['dataset'].unique()
list_two = train_qa['dataset'].unique()
all_ds_ids = list(set(list_one).union(set(list_two)))

TABLE_NUMBER = OUT_FOLDER.split('_')[-1]
TABLE_NUMBER = str(TABLE_NUMBER).zfill(3)
ds_id = [table for table in all_ds_ids if table.startswith(TABLE_NUMBER)]
ds_id = str(ds_id[0])

# select the specific dataset
filtered_qa = train_qa[train_qa['dataset'] == ds_id]
df = pd.read_parquet(f"data/{ds_id}.parquet")

# Load model and tokenizer with specified LLM_NAME
llm = AutoModelForCausalLM.from_pretrained(LLM_NAME, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(LLM_NAME, device_map="auto")
pipeline = pipeline("text-generation", model=llm, tokenizer=tokenizer, max_new_tokens=500, temperature=0.8, top_k=50, device_map="auto")

# Initialize HuggingFace pipeline
model = HuggingFacePipeline(pipeline=pipeline)

# System and user templates for question breakdown
system_template = """
You are an helpful assistant good at breaking down questions for a given table which is a pandas Dataframe.
Please break down the following question into smaller, more manageable steps. Each step should be an instruction in natural language that will be easily executable by one line of python code. All the steps as a whole should be able to solve the question if someone write a python code for each of them.

Also, attempt to write the code for each step in a way that it can be easily copy-pasted and run by someone who is not familiar with the question or the dataset.

Here is some information that will be useful for you to break down the questions : 
- The dataset is a pandas dataframe always
- The relevant columns will be given to you
- The types of the columns will be given to you, more information about all the types is given below
- The expected type of the answer will be given to you
- Make sure that the final answer follows the expected type of the answer
- The output is always of a single line
- First step is always to load the dataset
- Last step is always to print the answer

The types of the columns and the expected types of the answers are as follows :
- 'number' : represents a numerical value, for example, 1, 2.5, 3.14
- 'category' : represents a categorical value, for example, 'apple'. depends on the context which you'll have to infer
- 'date' : represents a date value, for example, 2022-01-01
- 'text' : represents a text value, for example, "Hello, World!", 'A quick brown fox...'
- 'boolean' : represents a boolean value, for example, True, False
- 'url' : represents a url value, for example, "https://www.google.com", 'abobe.com'
- 'list[number]' : represents a list of numerical values, for example, [1, 2, 3], [3.14, 2, 4.56]
- 'list[category]' : represents a list of categorical values, for example, ['apple', 'orange'], ['red', 'green', 'blue']
- 'list[url]' : represents a list of url values, for example, ["https://www.google.com", "https://www.bing.com"], ['abobe.com', 'microsoft.com']


Here are a few examples :
---
Example 1 :
---
Question : What is the average age of the people in the dataframe?
Dataset : 090_Students
All Columns : ['age', 'name']
Relevant Columns : ['age']
Type of the columns : ['number']
Type of the answer : number

Question Breakdown : 
1. Load the dataset
2. Filter out the column 'age' from the dataframe
3. Calculate the average age
4. Print the result

Code Attempt : 
```python
import pandas as pd
# Load the dataset
df = pd.read_parquet('data/090_Students.parquet')
# Filter out the column 'age' from the dataframe
age = df['age']
# Calculate the average age
average_age = age.mean()
# Print the result
print(average_age)
```
---
Example 2 :
---
Question : What is the salary of employee who has the highest performance rating?
Dataset : 090_Employees
All Columns : ['salary', 'performance_rating', 'employee_name', 'company_name', 'employee_id']
Relevant Columns : ['salary', 'performance_rating']
Type of the columns : ['number', 'number']
Type of the answer : number

Question Breakdown : 
1. Load the dataset
2. Filter out the columns 'salary' and 'performance_rating' from the dataframe
3. Filter the dataframe to get the employee with the highest performance rating
4. Get the salary of the employee
5. Print the result

Code Attempt :
```python
import pandas as pd
# Load the dataset
df = pd.read_parquet('data/090_Employees.parquet')
# Filter out the columns 'salary' and 'performance_rating' from the dataframe
df = df[['salary', 'performance_rating']]
# Filter the dataframe to get the employee with the highest performance rating
highest_performance_rating = df['performance_rating'].max()
employee = df[df['performance_rating'] == highest_performance_rating]
# Get the salary of the employee
salary = employee['salary']
# Print the result
print(salary)
```
---

Kindly be clear, concise and precise in your instructions.
"""

user_template = """
Question : {question}
Dataset : {dataset}
All Columns : {all_columns}
Relevant Columns : {columns}
Type of the columns : {column_types}
Type of the answer : {answer_type}
"""

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", user_template)]
)
output_parser = StrOutputParser()

# Iterate over filtered questions and save outputs
for i in tqdm(range(len(filtered_qa))):

    question = filtered_qa.iloc[i]['question']
    dataset_name = str(ds_id)
    all_columns = list(df.columns)
    columns = filtered_qa.iloc[i]['columns_used']
    column_types = filtered_qa.iloc[i]['column_types']
    answer_type = filtered_qa.iloc[i]['type']
    
    # Define the chain with templates
    chain = prompt_template | model | output_parser

    # Generate and save output
    output_one = chain.invoke({"question": question, "dataset": dataset_name, "all_columns": all_columns, "columns": columns, "column_types": column_types, "answer_type": answer_type})

    with open(f"{OUT_FOLDER}/question_{i}.txt", "w") as f:
        f.write(output_one)
