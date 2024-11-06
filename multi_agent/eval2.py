import re
import subprocess
import pandas as pd
from tqdm import tqdm

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

dev_qa = pd.read_parquet("dev_qa.parquet")
train_qa = pd.read_parquet("train_qa.parquet")

train_qa = pd.concat([train_qa, dev_qa])

list_one = dev_qa['dataset'].unique()
list_two = train_qa['dataset'].unique()

all_ds_ids = list(set(list_one).union(set(list_two)))
print(all_ds_ids)

start_table = 50
end_table = 65
total_questions = 0
correct_answers = 0
with open("output_answers.txt", "w") as output_file:
    # Loop through each table folder in the specified range
    for table_num in range(start_table, end_table + 1):
        folder = f'agent_two_table_{table_num}'
        table_num_str = str(table_num).zfill(3)
        ds_id = [table for table in all_ds_ids if table.startswith(table_num_str)]
        
        if not ds_id:
            print(f"No dataset found for table {table_num_str}")
            continue

        ds_id = str(ds_id[0])
        print(f"Evaluating dataset {ds_id} in folder {folder}")
        filtered_qa = train_qa[train_qa['dataset'] == ds_id]
        df = pd.read_parquet(f"data/{ds_id}.parquet")

        for i in tqdm(range(len(filtered_qa)), desc=f"Processing {folder}"):
            question = filtered_qa.iloc[i]['question']
            all_columns = list(df.columns)
            columns = filtered_qa.iloc[i]['columns_used']
            column_types = filtered_qa.iloc[i]['column_types']
            answer_type = filtered_qa.iloc[i]['type']
            answer = filtered_qa.iloc[i]['answer']
            
            # Load conversation for the current question
            with open(f'{folder}/question_{i}.txt', 'r') as file:
                conversation = file.read()

            # Extract the last code block
            code_blocks = re.findall(r'```python\n(.*?)\n```', conversation, re.DOTALL)
            if code_blocks:
                last_code_block = code_blocks[-1]
            else:
                print(f"No Python code block found in question {i} of {folder}")
                continue

            # Write and run the code block
            with open(f"{folder}/question_{i}.py", "w") as temp_file:
                temp_file.write(last_code_block)

            try:
                result = subprocess.run(
                    ["python", f"{folder}/question_{i}.py"],
                    capture_output=True,
                    text=True,
                    check=True
                )
                output_variable = result.stdout.strip()
            except subprocess.CalledProcessError as e:
                output_variable = f"Error: {e.stderr.strip()}"
                output_variable = ""
            
            if '\n' in output_variable:
                output_variable = output_variable.splitlines()[-1]

            output_file.write(f"{output_variable}\n")
            # Evaluate the answer
            is_correct = evaluator.default_compare(output_variable, answer, answer_type)
            correct_answers += int(is_correct)
            total_questions += 1

            # Display question result
            # print("---")
            # print(f"Question {i}:")
            # print("Captured Output:\n", output_variable)
            # print("Expected Answer:\n", answer)
            # print("Correct ? :", is_correct)
            # print("---")

# Calculate and print the accuracy score
accuracy = correct_answers / total_questions if total_questions > 0 else 0
print(f"Total Score: {correct_answers}/{total_questions}")
print(f"Accuracy: {accuracy:.2%}")