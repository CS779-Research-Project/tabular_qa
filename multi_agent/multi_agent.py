## HF_TOKEN = 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
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

dev_qa = pd.read_parquet("dev_qa.parquet")
train_qa = pd.read_parquet("train_qa.parquet")

list_one = dev_qa['dataset'].unique()
list_two = train_qa['dataset'].unique()

# merge the two lists
all_ds_ids = list(set(list_one).union(set(list_two)))
print(all_ds_ids)

ds_id = str('001_Forbes')
filtered_qa = train_qa[train_qa['dataset'] == ds_id]
df = pd.read_parquet(f"data/{ds_id}.parquet")

llm = AutoModelForCausalLM.from_pretrained("google/gemma-2-2b-it", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-2b-it", device_map="auto")
pipeline = pipeline("text-generation", model=llm, tokenizer=tokenizer, max_new_tokens=500, temperature=0.8, top_k=50, device_map="auto")

model = HuggingFacePipeline(pipeline=pipeline)

system_template = """
You are an helpful assistant good at breaking down questions for a given table which is a pandas Dataframe.
Please break down the following question into smaller, more manageable steps. Each step should be an instruction in natural language that will be easily executable by one line of python code. All the steps as a whole should be able to solve the question if someone write a python code for each of them.

Also, attempt to write the code for each step in a way that it can be easily copy-pasted and run by someone who is not familiar with the question or the dataset.

Here is some information that will be useful for you to break down the questions : 
- The dataset is a pandas dataframe always
- The relevant columns will be given to you
- The types of the columns will be given to you, more information about all the types is given below
- The expected type of the answer will be given to you
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
2. Filter the dataframe with the column 'age'
3. Calculate the average age
4. Print the result

Code Attempt : 
```python
import pandas as pd
# Load the dataset
df = pd.read_parquet('data/090_Students.parquet')
# Filter the dataframe with the column 'age'
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
2. Filter the dataframe with the columns 'salary' and 'performance_rating'
3. Filter the dataframe to get the employee with the highest performance rating
4. Get the salary of the employee
5. Print the result

Code Attempt :
```python
import pandas as pd
# Load the dataset
df = pd.read_parquet('data/090_Employees.parquet')
# Filter the dataframe with the columns 'salary' and 'performance_rating'
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
Tyep of the answer : {answer_type}
"""
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", user_template)]
)
output_parser = StrOutputParser()

# print("filtered_qa : ", filtered_qa.iloc[0])
for i in tqdm(range(len(filtered_qa))):

    # if i != 3:
    #     continue
    # get the question, columns, column_types and answer_type
    question = filtered_qa.iloc[i]['question']
    dataset_name = str(ds_id)
    all_columns = list(df.columns)
    columns = filtered_qa.iloc[i]['columns_used']
    column_types = filtered_qa.iloc[i]['column_types']
    answer_type = filtered_qa.iloc[i]['type']
    
    # make the chain
    chain = prompt_template | model | output_parser

    # invoke the chain
    output_one = chain.invoke({"question": question, "dataset": dataset_name, "all_columns": all_columns, "columns": columns, "column_types": column_types, "answer_type": answer_type})

    # redirect the output to a file
    # print(output_one)
    # assert False
    with open(f"forbes_agent_one/question_{i}.txt", "w") as f:
        f.write(output_one)
