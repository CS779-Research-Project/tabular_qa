import re
import subprocess
import pandas as pd
from tqdm import tqdm

from databench_eval.src.databench_eval import Evaluator

# Initialize evaluator and load data
evaluator = Evaluator()
dev_qa = pd.read_parquet("dev_qa.parquet")

# Initialize counters for accuracy calculation
total_questions = 0
correct_answers = 0

# Open output file to write answers
with open("output_answers.txt", "w") as output_file:
    # Loop through each row in dev_qa to maintain the original order
    for idx in tqdm(range(len(dev_qa)), desc="Processing dev_qa"):
        row = dev_qa.iloc[idx]
        ds_id = row['dataset']
        question = row['question']
        answer_type = row['type']
        answer = row['answer']
        
        # Load the corresponding data file
        df = pd.read_parquet(f"data/{ds_id}.parquet")
        
        # Load conversation for the current question
        folder = f'agent_two_table_{int(ds_id[:3])}'  # Assuming the folder name pattern includes the table prefix
        question_file = f'{folder}/question_{idx}.txt'
        try:
            with open(question_file, 'r') as file:
                conversation = file.read()
        except FileNotFoundError:
            print(f"File not found for question {idx} in dataset {ds_id}")
            output_file.write("\n")  # Write a blank line if file not found
            continue

        # Extract the last code block from the conversation
        code_blocks = re.findall(r'```python\n(.*?)\n```', conversation, re.DOTALL)
        if code_blocks:
            last_code_block = code_blocks[-1]
        else:
            print(f"No Python code block found in question {idx} of dataset {ds_id}")
            output_file.write("\n")  # Write a blank line if no code block is found
            continue

        # Write the code block to a temporary Python file
        temp_code_file = f"{folder}/question_{idx}.py"
        with open(temp_code_file, "w") as temp_file:
            temp_file.write(last_code_block)

        # Run the extracted code and capture the output
        try:
            result = subprocess.run(
                ["python", temp_code_file],
                capture_output=True,
                text=True,
                check=True
            )
            output_variable = result.stdout.strip()
            
            # Handle single-line or multi-line output
            if '\n' in output_variable:
                output_line = output_variable.splitlines()[-1]  # Capture only the last line of multi-line output
            else:
                output_line = output_variable  # Capture the whole single-line output

        except subprocess.CalledProcessError as e:
            output_variable = f"Error: {e.stderr.strip()}"
            output_line = ""  # Write a blank line on error

        # Write the answer to the output file
        output_file.write(f"{output_line}\n")

        # Evaluate the answer
        is_correct = evaluator.default_compare(output_variable, answer, answer_type)
        correct_answers += int(is_correct)
        total_questions += 1

        # Display question result in terminal
        print("---")
        print(f"Question {idx}:")
        print("Captured Output:\n", output_variable)
        print("Expected Answer:\n", answer)
        print("Correct ? :", is_correct)
        print("---")

# Calculate and print the accuracy score
accuracy = correct_answers / total_questions if total_questions > 0 else 0
print(f"Total Score: {correct_answers}/{total_questions}")
print(f"Accuracy: {accuracy:.2%}")
