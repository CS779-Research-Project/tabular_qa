import os
import time
import pprint
from tqdm import tqdm
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain.globals import set_verbose
import subprocess
import sys
import tempfile

set_verbose(True)

# Constants
MAX_TURNS = 20  # Maximum number of interactions
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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

# Define the Prompt Template for the Agentic LLM
AGENTIC_INITIAL_PROMPT = """
You are an AI assistant designed to perform multi-turn question answering using tabular data. Your objective is to break down the given question into a series of logical, achievable steps and then write code to handle each part. You will use Python with the pandas library to achieve this.

Please follow these guidelines:

1. **Understanding the Question:** Start by analyzing the question to identify its key components and sub-questions. If needed, rephrase or simplify the question to make it more manageable.
  
2. **Step-by-Step Plan:** Break the question down into smaller, executable steps. Each step should be specific and focus on one aspect of the question.

3. **Code Implementation:** For each step, generate Python code that accomplishes the task, using the pandas library where applicable. Ensure that your code is modular and easy to understand.

4. **Data Handling:** Use the following code line to load the dataset:
`df = pd.read_parquet(f"hf://datasets/cardiffnlp/databench/data/{ds_id}/all.parquet")`
If necessary, filter out the relevant columns from the table as provided by the user.

- For each step in the breakdown, include code that manipulates or analyzes the relevant data, including preprocessing, data extraction, or model inference, if applicable.

5. **Output Format:** The output format in which is the final answer should be presented is given by the user, the possible formats are : 
- "number" : The answer is a number, example: 42
- "text" : The answer is a text, example: "Hello, World!"
- "category" : The answer is a category, example: "apple"
- "date" : The answer is a date, example: "2022-01-01"
- "boolean" : The answer is a boolean, example: "True" or "False"
- "url" : The answer is a url, example: "google.com"
- "list[number]" : The answer is a list of numbers, example: [1, 2, 3]
- "list[category]" : The answer is a list of texts, example: ["apple", "banana", "cherry"]
- "list[url]" : The answer is a list of urls, example: ["google.com", "yahoo.com"]
Ensure that the final answer is clear, concise, and relevant to the original question and follows the output format. It should be printed using the `print()` function.

6. **Verification:** After generating the code for each step, include a brief explanation of how to verify the output's correctness.

**Example Workflow:**

1. **Break down the question:** Start by rephrasing or simplifying the original question into smaller, focused tasks.
   
2. **Write code for each task:** Write modular code snippets that accomplish each individual step, using tools and methods that are relevant.

3. **Combine the results:** Merge the outputs from each step to arrive at the final answer.

4. **Final answer validation:** Verify the consistency and accuracy of the final answer, ensuring that the outputs align with the original question.

**Constraints:**

- Make the code efficient and concise.
- Focus on readability and clear documentation.

**User Question:** {user_question}
**Relevant Columns:** {relevant_cols}
**Output Format:** {output_format}
**Dataset ID:** {ds_id}

Now, let's begin by breaking down the question provided and implementing the solution step by step.
"""

# Define the Prompt Template using LangChain
agentic_template = PromptTemplate(
    input_variables=["user_question", "relevant_cols", "ds_id", "output_format"],
    template=(AGENTIC_INITIAL_PROMPT)
)

# Initialize Memory for the Agentic LLM
message_history = ChatMessageHistory()
agentic_memory = ConversationBufferMemory(chat_memory=message_history, return_messages=True)

# Create the Agentic LLM Chain
def create_agentic_chain(llm):
    global agentic_template, agentic_memory

    # Creating the sequence using the memory, prompt, and LLM
    # The RunnableSequence will handle the order of execution
    agentic_chain = RunnableSequence(
        agentic_template,
        llm,
        StrOutputParser()
    )

    return agentic_chain

# Initialize the OpenAI LLM
def initialize_llm():
    """
    Initializes the OpenAI LLM using LangChain's OpenAI wrapper.
    """
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",  # Specify the model, can be changed to other versions
        temperature=0  # Control creativity of the responses
    )
    return llm

# Function to Execute Generated Code Safely
def execute_code(code, globals_dict=None, locals_dict=None):
    """
    Executes the given Python code in a controlled environment and captures the output or errors.
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
    """
    Logs each step of the interaction.
    """
    steps_log.append({
        "turn": turn,
        "action": action,
        "response": response
    })

# Main Agentic System Function
def agentic_system(user_question, relevant_cols, output_format, ds_id):
    """
    Orchestrates the multi-turn question answering process.
    """
    # Initialize LLM
    llm = initialize_llm()

    # Create Agentic Chain
    agentic_chain = create_agentic_chain(llm)

    # Initialize Variables
    turn_count = 0
    steps_log = []
    final_answer = None

    # Start Processing
    # while turn_count < MAX_TURNS:
    #     turn_count += 1
    #     print(f"\n--- Turn {turn_count} ---\n")
    start_time = time.time()
    
    # Prepare the prompt with current context
    agentic_input = {
        "ds_id": ds_id,
        "user_question": user_question,
        "relevant_cols": relevant_cols,
        "output_format": output_format
    }

    # Run Agentic LLM to get the response  
    try:
        agentic_response = agentic_chain.invoke(agentic_input)
    except Exception as e:
        print(f"Error in Agentic LLM: {e}")
        return None, steps_log
        # break

    # print("Agentic LLM Response:")
    # print(agentic_response)

    # Log the step
    log_step(steps_log, turn_count, "Agentic LLM Response", agentic_response)

    # Check if the Agentic LLM has provided the final answer
    # if "Final Answer:" in agentic_response:
    #     final_answer = agentic_response.split("Final Answer:")[-1].strip()
    #     print("\n--- Final Answer ---")
    #     print(final_answer)
        # break

    # Assume the Agentic LLM provides code snippets to execute
    if "```python" in agentic_response:
        code_start = agentic_response.find("```python") + len("```python")
        code_end = agentic_response.find("```", code_start)
        code = agentic_response[code_start:code_end].strip()
    else:
        print("No code block found in the Agentic LLM response.")
        return None, steps_log
        # break

    # print("\nGenerated Code:")
    # print(code)

    # Log the step
    log_step(steps_log, turn_count, "Generated Code", code)

    # Execute the code
    success, exec_output = execute_code(code)
    # also put the code in a file
    with open("code.py", "w") as f:
        f.write(code)

    if success:
        # print("\nExecution Output:")
        # print(exec_output)
        final_answer = exec_output
        # Provide the execution output back to the Agentic LLM as context
        user_question = f"{user_question}\nExecution Output:\n{exec_output}"
    else:
        print("\nExecution Error:")
        print(exec_output)
        final_answer = None
        # Provide the error back to the Agentic LLM for debugging
        user_question = f"{user_question}\nExecution Error:\n{exec_output}"

    end_time = time.time()
    # print("\nResponse Time: {:.2f} seconds".format(end_time - start_time))

    #     assert False
    # else:
    #     # If maximum turns reached without final answer
    #     print("\nMaximum number of turns reached. Process halted.")
    #     print("Steps carried out:")
    #     for step in steps_log:
    #         print(f"Turn {step['turn']}: {step['action']}")
    #         print(f"Response: {step['response']}\n")
    #     print("Please consider refining your question or increasing the number of allowed steps.")

    # Optionally, return the final answer and the log
    # assert False
    return final_answer, steps_log

# Example Usage
if __name__ == "__main__":
    # Initialize the LLMs with HuggingFacePipeline
    # Replace with your actual Hugging Face API token if required
    # For HuggingFacePipeline, authentication might not be necessary if using public models
    # If authentication is required, ensure that the environment is set up accordingly

    # User Question and Dataset ID
    # df_all_qa = pd.read_parquet('data/all_qa.parquet')
    # df_semeval_train_qa = pd.read_parquet('data/semeval_train_qa.parquet')
    df_semeval_dev_qa = pd.read_parquet('data/semeval_dev_qa.parquet')
    # ds_id = df_all_qa['dataset'][0] 
    # ds_id = '005_NYC'
    # get only those questions that have 'dataset' column equal to ds_id
    # df_all_qa = df_all_qa[df_all_qa['dataset'] == ds_id]
    # print("Total_questions :", len(df_all_qa))

    results = {}
    for i in tqdm(range(len(df_semeval_dev_qa))):
        df_row = df_semeval_dev_qa.iloc[i]
        user_question = df_row['question']
        relevant_cols = ', '.join(list(df_row['columns_used']))
        output_format = df_row['type']
        ds_id = df_row['dataset']
        # print(df_row)
        # assert False
        # Load the dataset using the provided code line
        # try:
        #     df = pd.read_parquet(f"hf://datasets/cardiffnlp/databench/data/{ds_id}/all.parquet")
        #     print("Dataset loaded successfully.")
        # except Exception as e:
        #     print(f"Error loading dataset: {e}")
        #     sys.exit(1)

        # Run the Agentic System
        print("The question is : ", user_question)
        print("The relevant columns are : ", relevant_cols)
        print("The output format is : ", output_format)
        print("The model answer is : ", df_row['answer'])
        print("The sample answer is : ", df_row['sample_answer'])
        final_answer, steps_log = agentic_system(user_question, relevant_cols, output_format, ds_id)
        print("The final answer is : ", final_answer)

        results[i] = {
            "question": user_question,
            "model_answer": final_answer,
            "sample_answer": df_row['sample_answer'],
            "answer": df_row['answer']
        }        
    
    # save the results in a json file
    import json
    with open(f'results_gpt_dev.json', 'w') as f:
        json.dump(results, f, indent=4)



    # if final_answer:
    #     print("\n=== Final Answer ===")
    #     print(final_answer)
    # else:
    #     print("\nNo final answer could be derived.")

    # Optionally, save the steps log to a file
    with open("steps_log.txt", "w") as log_file:
        for step in steps_log:
            log_file.write(f"Turn {step['turn']}:\nAction: {step['action']}\nResponse: {step['response']}\n\n")
    print("\nSteps log saved to 'steps_log.txt'.")