# Required Libraries
import os
import time
import pandas as pd
import torch
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate  # Corrected import path
from langchain_huggingface import HuggingFacePipeline
from langchain.memory import ConversationBufferMemory
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
from datasets import load_dataset
import bitsandbytes as bnb
import subprocess
import sys
import tempfile

# Constants
MAX_TURNS = 20  # Maximum number of interactions
MODEL_ID = "microsoft/Phi-3.5-mini-instruct"  # Hugging Face model ID
# HF_API_TOKEN = "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"  # Replace with your Hugging Face API token

# Initialize HuggingFace LLMs using HuggingFacePipeline
# def initialize_llm(model_id):
#     pipeline = HuggingFacePipeline.from_model_id(
#         model_id=model_id,
#         task="text-generation",
#         device_map="auto",
#         device=0,
#         pipeline_kwargs={
#             "max_new_tokens": 500,  # Adjust as needed
#             "top_k": 50,
#             "temperature": 0.1,
#         },
#     )
#     return pipeline

def get_next_row_generator(df):
    for _, row in df.iterrows():
        yield row

# Create the generator outside the function to keep track of the state
row_generator = None

def get_next_row(df):
    global row_generator
    if row_generator is None:
        # Initialize the generator if it's the first time or has been exhausted
        row_generator = get_next_row_generator(df)
    try:
        return next(row_generator)
    except StopIteration:
        # If the generator is exhausted, return a message or reset it
        row_generator = None
        return "No more rows available."

def initialize_llm(model_id):
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    #bng config
    bnb_config = BitsAndBytesConfig(
        load_in_8bit=True,  # Enable 8-bit quantization
    )

    # Load the model in 8-bit precision
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="balanced_low_0",  # Distribute the model across multiple GPUs
        quantization_config=bnb_config,
        max_length=4096,  # Maximum length of the generated text
    )

    hf_pipeline = pipeline(
        task="text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    pipe = HuggingFacePipeline(pipeline=hf_pipeline)

    return pipe


# Define the Initial Prompt for the Analyser LLM
ANALYSER_INITIAL_PROMPT = """
You are an Analyser LLM designed to help users obtain answers to their questions by coordinating with a Coder LLM. 

Your primary responsibilities include:

1. **Understanding the User's Question**: Comprehend the question provided by the user and determine the steps needed to derive the answer.
2. **Decomposing the Question**: Break down the question into smaller, manageable tasks that can be addressed sequentially.
3. **Interacting with the Coder LLM**: For each task, generate appropriate prompts to the Coder LLM to write or fix code required to execute that step.
4. **Analyzing Outputs and Errors**: Review the code outputs or errors returned by the Coder LLM, and decide on the next actions (e.g., debugging, refining prompts).
5. **Managing the Workflow**: Keep track of the steps taken and ensure the process progresses towards the final answer.
6. **Handling Turn Limits**: If the interaction exceeds a predefined number of turns (e.g., 20 turns), halt the process and provide a summary of the steps taken, along with any partial results.

**Guidelines:**

- **Clarity and Precision**: Ensure that each prompt to the Coder LLM is clear, precise, and contains all necessary information for accurate code generation.
- **Step-by-Step Progression**: Maintain a logical flow of tasks, ensuring each step builds upon the previous ones.
- **Error Handling**: When encountering errors in the code outputs, analyze and address them promptly by refining prompts or requesting corrections from the Coder LLM.
- **Termination Condition**: Monitor the number of interactions. If the process is not converging towards a solution within the turn limit, gracefully terminate and inform the user.

**Objective:**

Assist the user in obtaining accurate and efficient answers by effectively managing the interaction between the user, the Analyser LLM, and the Coder LLM. Strive for minimal turns while ensuring the correctness of the final answer.

---

**Example Workflow:**

1. **User Prompt**: "What is the average revenue of companies listed in the Forbes dataset for the year 2023?"
2. **Analyser LLM**:
   - Breaks down the question into tasks:
     1. Load the Forbes dataset.
     2. Filter data for the year 2023.
     3. Calculate the average revenue.
   - Sends prompts to the Coder LLM for each task sequentially.
3. **Coder LLM**: Returns code snippets for each task.
4. **Analyser LLM**: Executes code, handles any errors, and proceeds to the next step.
5. **Final Output**: Provides the average revenue to the user.

---

By defining the Analyser LLM with this prompt, you establish a clear framework for it to manage tasks, interact with the Coder LLM, and guide the user towards obtaining accurate answers efficiently.
"""

# Define the Prompt Template for the Analyser LLM
analyser_template = PromptTemplate(
    input_variables=["user_question"],
    template=ANALYSER_INITIAL_PROMPT + "\n\nUser Question: {user_question}\n\nAnalyser Response:"
)

# Initialize Memory for the Analyser LLM
analyser_memory = ConversationBufferMemory(memory_key="chat_history")

# Create the Analyser LLM Chain
def create_analyser_chain(llm):
    return LLMChain(
        llm=llm,
        prompt=analyser_template,
        memory=analyser_memory,
        verbose=True
    )

# Function to Load Specific Dataset
def load_specific_dataset(ds_id):
    df = pd.read_parquet(f"hf://datasets/cardiffnlp/databench/data/{ds_id}/all.parquet")
    semeval_train_qa = load_dataset("cardiffnlp/databench", name="semeval", split="train")
    specific_questions = semeval_train_qa.filter(lambda x: x['dataset'] == ds_id)
    return df, specific_questions

# Function to Execute Generated Code Safely
def execute_code(code):
    """
    Executes the given Python code in a temporary file and captures the output or errors.
    Returns a tuple of (success, output/error message).
    """
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as tmp_file:
            tmp_file.write(code)
            tmp_file_path = tmp_file.name
        # Execute the code and capture output
        result = subprocess.run(
            [sys.executable, tmp_file_path],
            capture_output=True,
            text=True,
            timeout=60  # seconds
        )
        os.unlink(tmp_file_path)  # Delete the temporary file
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
    except subprocess.TimeoutExpired:
        return False, "Execution timed out."
    except Exception as e:
        return False, str(e)

# Function to Log Steps
def log_step(steps_log, turn, action, response):
    steps_log.append({
        "turn": turn,
        "action": action,
        "response": response
    })

# Main Agentic System Function
def agentic_system(question_row, ds_id, model_id): # the user_question and the dataset id is passed into the input, the model id is fixed globally
    # user_question -> question_row
    # Initialize LLMs
    analyser_llm = initialize_llm(model_id)
    coder_llm = initialize_llm(model_id)  # Assuming same model for simplicity

    # Create Analyser Chain
    analyser_chain = create_analyser_chain(analyser_llm)

    # Load Dataset
    # try:
    #     df, questions = load_specific_dataset(ds_id)
    # except Exception as e:
    #     print(f"Error loading dataset: {e}")
    #     return

    # Initialize Variables
    turn_count = 0
    steps_log = []
    final_answer = None

    # Start Processing
    # analyser_input = user_question
    analyser_input = question_row['question']

    while turn_count < MAX_TURNS:
        turn_count += 1
        print(f"\n--- Turn {turn_count} ---\n")
        start_time = time.time()
        # Run Analyser LLM to get the response  
        try:
            # analyser_response = analyser_chain.run(user_question=analyser_input)
            analyser_response = analyser_chain.run(user_question=analyser_input)
        except Exception as e:
            print(f"Error in Analyser LLM: {e}")
            break

        print("Analyser LLM Response:")
        print(analyser_response)

        # save this response to a file 
        with open("analyser_response.txt", "w") as log_file:
            log_file.write(f"Turn {turn_count}:\nAction: Analyser LLM Response\nResponse: {analyser_response}\n\n")

        end_time = time.time()
        print("\n\n\n\n\n\n\n Response Time : ", end_time - start_time)
        assert False

        # Log the step
        log_step(steps_log, turn_count, "Analyser LLM Response", analyser_response)

        # Check if the Analyser has provided the final answer
        if "Final Answer:" in analyser_response:
            final_answer = analyser_response.split("Final Answer:")[-1].strip()
            print("\n--- Final Answer ---")
            print(final_answer)
            break

        # Assume the Analyser LLM provides code snippets to execute
        # Extract the code block from the response
        if "```python" in analyser_response:
            code_start = analyser_response.find("```python") + len("```python")
            code_end = analyser_response.find("```", code_start)
            code = analyser_response[code_start:code_end].strip()
        else:
            print("No code block found in the Analyser response.")
            break

        print("\nCoder LLM Code:")
        print(code)

        # Log the step
        log_step(steps_log, turn_count, "Coder LLM Code", code)

        # Execute the code
        success, exec_output = execute_code(code)

        if success:
            print("\nExecution Output:")
            print(exec_output)
            # Provide the execution output back to the Analyser LLM as context
            analyser_input = f"Execution Output:\n{exec_output}"
        else:
            print("\nExecution Error:")
            print(exec_output)
            # Provide the error back to the Analyser LLM for debugging
            analyser_input = f"Execution Error:\n{exec_output}"

    else:
        # If maximum turns reached without final answer
        print("\nMaximum number of turns reached. Process halted.")
        print("Steps carried out:")
        for step in steps_log:
            print(f"Turn {step['turn']}: {step['action']}")
            print(f"Response: {step['response']}\n")
        print("Please consider refining your question or increasing the number of allowed steps.")

    # Optionally, return the final answer and the log
    return final_answer, steps_log

# Example Usage
if __name__ == "__main__":
    # Initialize the LLMs with HuggingFacePipeline
    # Replace with your actual Hugging Face API token if required
    # For HuggingFacePipeline, authentication might not be necessary if using public models
    # If authentication is required, ensure that the environment is set up accordingly

    # User Question and Dataset ID
    # user_question = "What is the average revenue of companies listed in the Forbes dataset for the year 2023?"
    # ds_id = "001_Forbes"    
    # all_qa = load_dataset("cardiffnlp/databench", name="qa", split="train")
    # semeval_train_qa = load_dataset("cardiffnlp/databench", name="semeval", split="train")
    # semeval_dev_qa = load_dataset("cardiffnlp/databench", name="semeval", split="dev")

    # # Save datasets to Parquet files in the 'data' folder
    # all_qa.to_parquet('data/all_qa.parquet')
    # semeval_train_qa.to_parquet('data/semeval_train_qa.parquet')
    # semeval_dev_qa.to_parquet('data/semeval_dev_qa.parquet')

    # # Load the datasets using pandas
    df_all_qa = pd.read_parquet('data/all_qa.parquet')
    df_semeval_train_qa = pd.read_parquet('data/semeval_train_qa.parquet')
    df_semeval_dev_qa = pd.read_parquet('data/semeval_dev_qa.parquet')
    ds_id = df_all_qa['dataset'][0] 
    # df = pd.read_parquet(f"hf://datasets/cardiffnlp/databench/data/{ds_id}/all.parquet") # for loading all the dataset.
    # df = pd.read_parquet(f"hf://datasets/cardiffnlp/databench/data/{ds_id}/sample.parquet") # for loading a sample of the dataset.
    # print(df)
    # print(len(all_qa))
    df_row = get_next_row(df_all_qa)
    # print(df_row)
    # user_question = df_row['question']



    # assert False
    # Run the Agentic System
    final_answer, steps_log = agentic_system(df_row, ds_id, MODEL_ID)
    assert False
    if final_answer:
        print("\n=== Final Answer ===")
        print(final_answer)
    else:
        print("\nNo final answer could be derived.")

    # Optionally, save the steps log to a file
    with open("steps_log.txt", "w") as log_file:
        for step in steps_log:
            log_file.write(f"Turn {step['turn']}:\nAction: {step['action']}\nResponse: {step['response']}\n\n")
    print("\nSteps log saved to 'steps_log.txt'.")
