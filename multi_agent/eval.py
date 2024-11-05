import re
import subprocess
import pandas as pd

from databench_eval.src.databench_eval import Evaluator

evaluator = Evaluator()

def default_compare(self, value, truth, semantic):
        if semantic == "boolean":
            return str(value) == str(truth)
        elif semantic == "category":
            return str(value) == str(truth)
        elif semantic == "number":
            try:
                value_cleaned = ''.join(char for char in str(value) if char.isdigit() or char in ['.', '-'])
                truth_cleaned = ''.join(char for char in str(truth) if char.isdigit() or char in ['.', '-'])
                return round(float(value_cleaned), 2) == round(float(truth_cleaned), 2)
            except:
                return False
        elif semantic == "list[category]":
            try:
                value_list = [item.strip() for item in str(value).strip('[]').split(',')]
                truth_list = [item.strip() for item in str(truth).strip('[]').split(',')]
                if len(value_list) != len(truth_list):
                    return False
                
                return set(value_list) == set(truth_list)
            except Exception as exc:
                return False

        elif semantic == "list[number]":
            try:
                value_list = sorted(round(float(''.join(c for c in v.strip() if c.isdigit() or c in ['.', '-'])), 2) for v in str(value).strip('[]').split(',') if v.strip())
                truth_list = sorted(round(float(''.join(c for c in t.strip() if c.isdigit() or c in ['.', '-'])), 2) for t in str(truth).strip('[]').split(',') if t.strip())
                
                if len(value_list) != len(truth_list):
                    return False
                
                return set(value_list) == set(truth_list)
            except Exception as exc:
                return False

        else:
            raise Exception(f"Semantic not supported: {semantic}")

FOLDER = 'forbes_agent_two_ms'

dev_qa = pd.read_parquet("dev_qa.parquet")
train_qa = pd.read_parquet("train_qa.parquet")

list_one = dev_qa['dataset'].unique()
list_two = train_qa['dataset'].unique()

all_ds_ids = list(set(list_one).union(set(list_two)))
print(all_ds_ids)

FOLDER = 'agent_one_table_50'
TABLE_NUMBER = FOLDER.split('_')[-1]
TABLE_NUMBER = str(TABLE_NUMBER).zfill(3)
ds_id = [table for table in all_ds_ids if table.startswith(TABLE_NUMBER)]
ds_id = str(ds_id[0])
filtered_qa = train_qa[train_qa['dataset'] == ds_id]
df = pd.read_parquet(f"data/{ds_id}.parquet")

score = 0

for i in range(25):
    question = filtered_qa.iloc[i]['question']
    dataset_name = str(ds_id)
    all_columns = list(df.columns)
    columns = filtered_qa.iloc[i]['columns_used']
    column_types = filtered_qa.iloc[i]['column_types']
    answer_type = filtered_qa.iloc[i]['type']
    answer = filtered_qa.iloc[i]['answer']
    with open(f'{FOLDER}/question_{i}.txt', 'r') as file:
        conversation = file.read()

    # Step 1: Extract the last code block
    code_blocks = re.findall(r'```python\n(.*?)\n```', conversation, re.DOTALL)
    if code_blocks:
        last_code_block = code_blocks[-1]  # Get the last code block
    else:
        raise ValueError("No Python code block found in the input string.")

    # Step 2: Write the code block to a temporary file
    with open(f"{FOLDER}/question_{i}.py", "w") as temp_file:
        temp_file.write(last_code_block)

    # Step 3: Run the temporary Python file and capture its output
    try:
        result = subprocess.run(
            ["python", f"{FOLDER}/question_{i}.py"],
            capture_output=True,
            text=True,
            check=True
        )
        output_variable = result.stdout.strip()  # Store the output in a variable
    except subprocess.CalledProcessError as e:
        output_variable = f"Error: {e.stderr.strip()}"
    # finally:
        # Clean up the temporary file
        # import os
        # os.remove("temp_code.py")
    # Print the output stored in output_variable
    print("---")
    print(f"Question {i}:")
    print("Captured Output:\n", output_variable)
    print("Expected Answer:\n", answer)
    # print("Correct ? : ", evaluator.default_compare(output_variable, answer, answer_type))
    score += int(evaluator.default_compare(output_variable, answer, answer_type))
    print("---")

print("Total Score : ", score)