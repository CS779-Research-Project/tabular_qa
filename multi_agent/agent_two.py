## HF_TOKEN = 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
import re
import io
import sys

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

DS_ID = "001_Forbes"

dev_qa = pd.read_parquet("dev_qa.parquet")
train_qa = pd.read_parquet("train_qa.parquet")

list_one = dev_qa['dataset'].unique()
list_two = train_qa['dataset'].unique()

all_ds_ids = list(set(list_one).union(set(list_two)))
print(all_ds_ids)

llm = AutoModelForCausalLM.from_pretrained("google/gemma-2-2b-it", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-2b-it", device_map="auto")
pipeline = pipeline("text-generation", model=llm, tokenizer=tokenizer, max_new_tokens=500, temperature=0.8, top_k=50, device_map="auto")

model = HuggingFacePipeline(pipeline=pipeline)

def get_agent_one_response(question_id = 0):
    with open(f"forbes_agent_one/question_{question_id}.txt", "r") as file:
        text_content = file.read()

    human_section_start = text_content.find("Human:")
    human_section = text_content[human_section_start:].strip() if human_section_start != -1 else "No Human section found"
    
    question_breakdown_start = text_content.rfind("Question Breakdown :")
    code_attempt_start = text_content.rfind("Code Attempt :")
    
    question_breakdown_section = text_content[question_breakdown_start:code_attempt_start].strip() if question_breakdown_start != -1 else "No Question Breakdown section found"
    code_attempt_section = text_content[code_attempt_start:].strip() if code_attempt_start != -1 else "No Code Attempt section found"

    return human_section, question_breakdown_section, code_attempt_section 

# ds_id = str(DS_ID)
# df = pd.read_parquet(f"data/{ds_id}.parquet")
# filtered_qa = train_qa[train_qa['dataset'] == ds_id]

system_template = """
You are a verification and troubleshooting assistant designed to assess, validate, and refine code logic and outputs generated by a first agent. Your role is to:

1. Verify Code Steps: Ensure each step in the code breakdown is accurate, logically sequenced, and follows the requirements.
2. Validate Execution & Output:
   - Review each code line to confirm it performs as intended.
   - Check that the output type and format match the specified requirements.
3. Troubleshoot & Suggest Improvements:
   - Identify issues, such as logic errors or inefficiencies, and suggest precise improvements.
   - Provide specific code modifications to correct issues and enhance clarity.
4. Ensure Clarity: Keep suggestions concise and actionable, tailored for those unfamiliar with the dataset or question context.

When generating your response, follow the given format as strictly as possible:

Re-attempted Code with Modifications: 

```python
# Your modified code here
```

Here are a few examples : 
---
Example 1 :
---
Here is the conversation with the first agent : 

Question : Is there a non-self-made billionaire in the top 5 ranks?
Dataset : 001_Forbes
All Columns : ['rank', 'personName', 'age', 'finalWorth', 'category', 'source', 'country', 'state', 'city', 'organization', 'selfMade', 'gender', 'birthDate', 'title', 'philanthropyScore', 'bio', 'about']
Relevant Columns : ['rank', 'selfMade']
Type of the columns : ['number[uint16]', 'boolean']
Type of the answer : boolean
 
Question Breakdown : 
1. Load the dataset
2. Filter the dataframe with the column 'rank'
3. Filter the dataframe with the column'selfMade'
4. Check if the filtered dataframe has any non-self-made billionaires in the top 5 ranks
5. Print the result

Code Attempt :
```python
import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'rank'
rank = df['rank']
# Filter the dataframe with the column'selfMade'
selfMade = df['selfMade']
# Check if the filtered dataframe has any non-self-made billionaires in the top 5 ranks
non_self_made_billionaires = rank.isin([1, 2, 3, 4, 5])
# Print the result
print(non_self_made_billionaires)
```

Here is the output of the code-block present in the above conversation : 
0        True
1        True
2        True
3        True
4        True
        ...  
2663    False
2664    False
2665    False
2666    False
2667    False
Name: rank, Length: 2668, dtype: bool

Observations and Changes Made : 
1. The output does not match the expected answer type.
2. The code uses the relevant columns and no other columns.
2. Modify the filtering condition to check for non-self-made billionaires in the top 5 ranks.
2. Adjust the print statement to display the correct result that follows the output format.

Re-attempted Code with Modifications : 

```python
import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'rank'
rank = df['rank']
# Filter the dataframe with the column'selfMade'
selfMade = df['selfMade']
# Check if the filtered dataframe has any non-self-made billionaires in the top 5 ranks
non_self_made_billionaires = df[(rank.isin([1, 2, 3, 4, 5]) & selfMade.isin([False]))]
# Print the result
print(non_self_made_billionaires.empty)
```

---
Example 2 :
---

Here is the conversation with the first agent :

Question : Is the person with the highest net worth self-made?
Dataset : 001_Forbes
All Columns : ['rank', 'personName', 'age', 'finalWorth', 'category', 'source', 'country', 'state', 'city', 'organization', 'selfMade', 'gender', 'birthDate', 'title', 'philanthropyScore', 'bio', 'about']
Relevant Columns : ['finalWorth', 'selfMade']
Type of the columns : ['number[uint32]', 'boolean']
Tyep of the answer : boolean
 
Question Breakdown : 
1. Load the dataset
2. Filter the dataframe with the column 'finalWorth'
3. Filter the dataframe with the column'selfMade'
4. Get the person with the highest net worth
5. Check if the person is self-made
6. Print the result

Code Attempt :
```python
import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'finalWorth'
df = df[df['finalWorth'] == df['finalWorth'].max()]
# Filter the dataframe with the column'selfMade'
df = df[df['selfMade'] == True]
# Get the person with the highest net worth
highest_net_worth = df['finalWorth'].max()
# Check if the person is self-made
is_self_made = df['selfMade'].max()
# Print the result
print(is_self_made)
```

Here is the output of the code-block present in the above conversation :
True

Observations and Changes Made : 
There are no changes to be made in the code as it is already correct and follows the expected answer type and uses the relevant columns.

Re-attempted Code with Modifications: 

```python
import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'finalWorth'
df = df[df['finalWorth'] == df['finalWorth'].max()]
# Filter the dataframe with the column'selfMade'
df = df[df['selfMade'] == True]
# Get the person with the highest net worth
highest_net_worth = df['finalWorth'].max()
# Check if the person is self-made
is_self_made = df['selfMade'].max()
# Print the result
print(is_self_made)
```

---

Be as detailed and specific as possible in your responses to ensure the first agent can effectively learn from your feedback and improve their code logic and execution.
"""

user_template = """
Here is the conversation with the first agent : 
{first_conversation}

Here is the output of the code-block present in the above conversation : 
{code_output}

"""

# Kindly write the code with the changes if there are any, or else re-write the same code.

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", user_template)]
)

# prompt = prompt_template.invoke({"first_conversation" : human_section, "code_output" : execution_output})

# print(prompt)

output_parser = StrOutputParser() 
chain = prompt_template | model | output_parser

for i in tqdm(range(25)):
    human_section, question_breakdown_section, code_attempt_section = get_agent_one_response(i)
    code_match = re.search(r"```python(.*?)```", code_attempt_section, re.DOTALL)

    if code_match:
        code = code_match.group(1).strip()
    else:
        code = ""

    # Redirect stdout and stderr to capture execution output and error messages
    output = io.StringIO()
    sys.stdout = output
    sys.stderr = output

    # Execute the extracted code
    try:
        exec(code)
    except Exception as e:
        # Capture any exceptions
        print(f"Error: {e}")

    # Reset stdout and stderr to normal
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    # Get all the output in one variable
    execution_output = output.getvalue()
    output.close()
    output_one = chain.invoke({"first_conversation" : human_section[7:], "code_output" : execution_output})
    with open(f"forbes_agent_two/question_{i}.txt", "w") as file:
        file.write(output_one)