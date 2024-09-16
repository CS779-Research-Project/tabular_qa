import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
import bitsandbytes as bnb
from tqdm import tqdm
import re

NUM_SAMPLES = 10

def parse_final_answer(response):
    lines_with_answer = [line.split("Final Answer: ")[-1].strip() 
                            for line in response.splitlines() if "Final Answer: " in line]
    return lines_with_answer[-1]

def extract_from_nth_action_input(text, n):
    # Split the input text into lines
    lines = text.splitlines()

    # Initialize a counter to track occurrences of "Action Input:"
    action_input_count = 0

    # Flag to start collecting lines after the nth occurrence of "Action Input:"
    collecting = True
    action_input_spotted = False

    # List to hold lines from the nth "Action Input:" to the line before "Observation"
    extracted_lines = []

    for line in lines:
        # Check if the line starts with "Action Input:"
        if line.startswith("Action Input:"):
            action_input_count += 1

            # Start collecting lines after reaching the nth "Action Input:"
            if action_input_count == n:
                action_input_spotted = True

        # Stop collecting lines at the next "Observation" line
        if collecting:
            if line.startswith("Observation") and action_input_spotted:
                break
            extracted_lines.append(line)

    # Join the extracted lines back into a single string
    extracted_text = "\n".join(extracted_lines)

    return extracted_text

def truncate_at_second_action_input(text, n):
    # Split the input text into lines
    lines = text.splitlines()

    # Initialize a counter to track occurrences of "Action Input:"
    action_input_count = 0

    # List to hold lines up to the second occurrence of "Action Input:"
    truncated_lines = []

    for line in lines:
        truncated_lines.append(line)
        if line.startswith("Action Input:"):
            action_input_count += 1

        # Stop adding lines after the second occurrence
        if action_input_count == n:
            break

    # Join the truncated lines back into a single string
    truncated_text = "\n".join(truncated_lines)

    return truncated_text

def stop(prompt, response):
    # remove the overlapping part of the prompt and response
    prompt_lines = prompt.splitlines()
    response_lines = response.splitlines()
    # print("THE PROMPT LINES ARE: ", prompt_lines[50:])
    # print("THE RESPONSE LINES ARE: ", response_lines[50:])
    for i, (prompt_line, response_line) in enumerate(zip(prompt_lines, response_lines)):
        # if prompt_line != response_line:

        if prompt_line.strip() != response_line.strip():
            # print("THE PROMPT LINE IS: ", prompt_line)
            # print("THE RESPONSE LINE IS: ", response_line)
            break
    # print("\n".join(response_lines[i:]))
    # print("THE PROMPT IS: ", prompt)
    # print("THE RESPONSE IS: ", response)
    string = "\n".join(response_lines[i+1:])
    # final_answer_pattern = r"Thought:.*\nFinal Answer:"
    final_answer_pattern = r"^\s*Thought:.*\nFinal Answer:"
    if re.match(final_answer_pattern, string, re.DOTALL):
        # print("THE STRING MATCHES THE PATTERN AND THE RESPONSE IS: ", string)
        # assert False
        return True
    else:
        # print("THE STRING DOES NOT MATCH THE PATTERN AND THE RESPONSE IS: ", string)
        return False


splits_q = {'001_Forbes': 'data/001_Forbes/qa.parquet', '002_Titanic': 'data/002_Titanic/qa.parquet', '003_Love': 'data/003_Love/qa.parquet', '004_Taxi': 'data/004_Taxi/qa.parquet', '005_NYC': 'data/005_NYC/qa.parquet', '006_London': 'data/006_London/qa.parquet', '007_Fifa': 'data/007_Fifa/qa.parquet', '008_Tornados': 'data/008_Tornados/qa.parquet', '009_Central': 'data/009_Central/qa.parquet', '010_ECommerce': 'data/010_ECommerce/qa.parquet', '011_SF': 'data/011_SF/qa.parquet', '012_Heart': 'data/012_Heart/qa.parquet', '013_Roller': 'data/013_Roller/qa.parquet', '014_Airbnb': 'data/014_Airbnb/qa.parquet', '015_Food': 'data/015_Food/qa.parquet', '016_Holiday': 'data/016_Holiday/qa.parquet', '017_Hacker': 'data/017_Hacker/qa.parquet', '018_Staff': 'data/018_Staff/qa.parquet', '019_Aircraft': 'data/019_Aircraft/qa.parquet', '020_Real': 'data/020_Real/qa.parquet', '021_Telco': 'data/021_Telco/qa.parquet', '022_Airbnbs': 'data/022_Airbnbs/qa.parquet', '023_Climate': 'data/023_Climate/qa.parquet', '024_Salary': 'data/024_Salary/qa.parquet', '025_Data': 'data/025_Data/qa.parquet', '026_Predicting': 'data/026_Predicting/qa.parquet', '027_Supermarket': 'data/027_Supermarket/qa.parquet', '028_Predict': 'data/028_Predict/qa.parquet', '029_NYTimes': 'data/029_NYTimes/qa.parquet', '030_Professionals': 'data/030_Professionals/qa.parquet', '031_Trustpilot': 'data/031_Trustpilot/qa.parquet', '032_Delicatessen': 'data/032_Delicatessen/qa.parquet', '033_Employee': 'data/033_Employee/qa.parquet', '034_World': 'data/034_World/qa.parquet', '035_Billboard': 'data/035_Billboard/qa.parquet', '036_US': 'data/036_US/qa.parquet', '037_Ted': 'data/037_Ted/qa.parquet', '038_Stroke': 'data/038_Stroke/qa.parquet', '039_Happy': 'data/039_Happy/qa.parquet', '040_Speed': 'data/040_Speed/qa.parquet', '041_Airline': 'data/041_Airline/qa.parquet', '042_Predict': 'data/042_Predict/qa.parquet', '043_Predict': 'data/043_Predict/qa.parquet', '044_IMDb': 'data/044_IMDb/qa.parquet', '045_Predict': 'data/045_Predict/qa.parquet', '046_120': 'data/046_120/qa.parquet', '047_Bank': 'data/047_Bank/qa.parquet', '048_Data': 'data/048_Data/qa.parquet', '049_Boris': 'data/049_Boris/qa.parquet', '050_ING': 'data/050_ING/qa.parquet', '051_Pokemon': 'data/051_Pokemon/qa.parquet', '052_Professional': 'data/052_Professional/qa.parquet', '053_Patents': 'data/053_Patents/qa.parquet', '054_Joe': 'data/054_Joe/qa.parquet', '055_German': 'data/055_German/qa.parquet', '056_Emoji': 'data/056_Emoji/qa.parquet', '057_Spain': 'data/057_Spain/qa.parquet', '058_US': 'data/058_US/qa.parquet', '059_Second': 'data/059_Second/qa.parquet', '060_Bakery': 'data/060_Bakery/qa.parquet', '061_Disneyland': 'data/061_Disneyland/qa.parquet', '062_Trump': 'data/062_Trump/qa.parquet', '063_Influencers': 'data/063_Influencers/qa.parquet', '064_Clustering': 'data/064_Clustering/qa.parquet', '065_RFM': 'data/065_RFM/qa.parquet'}

splits_full = {}
for k, v in splits_q.items():
    splits_full[k] = v.replace("qa", "all")

splits_lite = {}
for k, v in splits_q.items():
    splits_lite[k] = v.replace("qa", "sample")

df = pd.read_parquet("hf://datasets/cardiffnlp/databench/" + splits_lite['003_Love'])
df_q = pd.read_parquet("hf://datasets/cardiffnlp/databench/" + splits_q['003_Love'])

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3.5-mini-instruct")
# bnb_config = BitsAndBytesConfig(
#     load_in_4bit=True,  # Enable 4-bit quantization
#     bnb_4bit_use_double_quant=True,  # Enable double quantization for better accuracy
#     bnb_4bit_quant_type="nf4",  # Set quantization type to 'nf4' for optimized precision
#     bnb_4bit_compute_dtype=torch.float16  # Use float16 for stable computation
# )
bnb_config = BitsAndBytesConfig(
    load_in_8bit=True,  # Enable 4-bit quantization
)

# assert False
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3.5-mini-instruct",
    device_map="auto",  # Automatically maps model layers to the available GPUs or CPU
    quantization_config=bnb_config
    # torch_dtype = torch.float16
)

results = {}

for k, v in list(splits_q.items()):
    print("Currently on dataset: ", k)
    results[k] = {}
    df_path = "data/lite/" + f"{k}.parquet"
    df_q_path = "data/questions/" + f"{k}.parquet"
    df = pd.read_parquet(df_path)
    df_q = pd.read_parquet("data/questions/" + f"{k}.parquet")

    try:
        for i, row in tqdm(df_q.iterrows(), total=len(df_q)):
            # TODO 
            title = k
            table_head_md = df.head().to_markdown()
            question = row["question"]
            answer_type = row["type"]
            prompt = f"""
You are working with a pandas dataframe in Python. The name of the dataframe is `df`. Your task is to use `python_repl_ast` to answer the question posed to you.

Tool Description:
- `python_repl_ast`: A Python shell. Use this to execute python commands. Input should be a valid python command. When using this tool, sometimes the output is abbreviated - ensure it does not appear abbreviated before using it in your answer.

Guidelines:
- **Aggregated Rows**: Be cautious of rows that aggregate data such as 'total', 'sum', or 'average'. Ensure these rows do not influence your results inappropriately.
- **Data Verification**: Before concluding the final answer, always verify that your observations align with the original table and question.

Strictly follow the given format to respond:

Question: the input question you must answer
Thought: you should always think about what to do to interact with `python_repl_ast`
Action: can **ONLY** be `python_repl_ast`
Action Input: the input code to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: after verifying the table, observations, and the question, I am confident in the final answer
Final Answer: the final answer to the original input question (AnswerName1, AnswerName2...)

Notes for final answer:
- Ensure the final answer format is only "Final Answer: <{answer_type}>" form, no other form.
- Ensure the final answer is a number or entity names, as short as possible, without any explanation.
- Ensure to have a concluding thought that verifies the table, observations and the question before giving the final answer.

You are provided with a table regarding "{title}". This is the result of `print(df.head().to_markdown())`:

{table_head_md}

**Note**: All cells in the table should be considered as `object` data type, regardless of their appearance.

Begin!
Question : {question}
"""
            all_answers = []
            for _ in range(NUM_SAMPLES):
                next_prompt = prompt
                N = 2
                while True:
                    inputs = tokenizer(next_prompt, return_tensors="pt").to(model.device)
                    generate_ids = model.generate(
                       inputs.input_ids, 
                       max_new_tokens=300,
                       do_sample = True,
                       temperature = 0.8
                    )

                    # Decode the output
                    response = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

                    if stop(next_prompt, response) == True:
                        ans = parse_final_answer(response)
                        # print("THE FINAL ANSWER IS: ", ans)
                        # print("THE ACTUAL ANSWER IS: ", row['answer'])
                        all_answers.append(ans)
                        break
                    # print(response)
                    # truncated_response = truncate_at_second_action_input(response, N)
                    truncated_response = extract_from_nth_action_input(response, N)
                    N += 1
                    # print(truncated_response)
                    # print response in a file
                    # with open("response.txt", "w") as f:
                    #     f.write(response)

                    ## extract the Action Input from the response
                    lines_with_answer = [line.split("Action Input: ")[-1].strip() 
                                    for line in truncated_response.splitlines() if "Action Input: " in line]
                    
                    # Truncate the response at Action Input's line

                    
                    # print("LINES WITH ANSWER : ",lines_with_answer)
                    code_to_execute = "exec_res = " + lines_with_answer[-1]

                    exec_globals = {'df': df}  # Define the globals that exec will use
                    exec_locals = {}  # Define the locals that exec will use
                    try:
                        exec(code_to_execute, exec_globals, exec_locals)
                    except Exception as e:
                        print(f"Error during execution: {e}")

                    # Capture and print the final answer if available
                    exec_res = exec_locals.get('exec_res', 'No final answer found.')

                    next_prompt = f"""{truncated_response}
Observation : The result of the action was {exec_res}
"""         
            # print("THE ANSWERS ARE: ", all_answers)
            results[k][i] = {"question": question, "model_answer": all_answers, "sample_answer" : row['sample_answer'], "answer": row['answer']}

    except Exception as e:
        print(e)
        continue    

import json

with open("pyagent_phi35_sc_lite.json", "w") as f:
    json.dump(results, f, indent=4)