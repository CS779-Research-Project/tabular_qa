import io
import contextlib
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, BitsAndBytesConfig
import torch
import bitsandbytes as bnb
from tqdm import tqdm
from langchain_core.prompts import PromptTemplate  # Updated import path
from langchain.chains import LLMChain  # Updated import path
from langchain_huggingface import HuggingFacePipeline
from langchain.chains import SequentialChain

splits_q = {'001_Forbes': 'data/001_Forbes/qa.parquet', '002_Titanic': 'data/002_Titanic/qa.parquet', '003_Love': 'data/003_Love/qa.parquet', '004_Taxi': 'data/004_Taxi/qa.parquet', '005_NYC': 'data/005_NYC/qa.parquet', '006_London': 'data/006_London/qa.parquet', '007_Fifa': 'data/007_Fifa/qa.parquet', '008_Tornados': 'data/008_Tornados/qa.parquet', '009_Central': 'data/009_Central/qa.parquet', '010_ECommerce': 'data/010_ECommerce/qa.parquet', '011_SF': 'data/011_SF/qa.parquet', '012_Heart': 'data/012_Heart/qa.parquet', '013_Roller': 'data/013_Roller/qa.parquet', '014_Airbnb': 'data/014_Airbnb/qa.parquet', '015_Food': 'data/015_Food/qa.parquet', '016_Holiday': 'data/016_Holiday/qa.parquet', '017_Hacker': 'data/017_Hacker/qa.parquet', '018_Staff': 'data/018_Staff/qa.parquet', '019_Aircraft': 'data/019_Aircraft/qa.parquet', '020_Real': 'data/020_Real/qa.parquet', '021_Telco': 'data/021_Telco/qa.parquet', '022_Airbnbs': 'data/022_Airbnbs/qa.parquet', '023_Climate': 'data/023_Climate/qa.parquet', '024_Salary': 'data/024_Salary/qa.parquet', '025_Data': 'data/025_Data/qa.parquet', '026_Predicting': 'data/026_Predicting/qa.parquet', '027_Supermarket': 'data/027_Supermarket/qa.parquet', '028_Predict': 'data/028_Predict/qa.parquet', '029_NYTimes': 'data/029_NYTimes/qa.parquet', '030_Professionals': 'data/030_Professionals/qa.parquet', '031_Trustpilot': 'data/031_Trustpilot/qa.parquet', '032_Delicatessen': 'data/032_Delicatessen/qa.parquet', '033_Employee': 'data/033_Employee/qa.parquet', '034_World': 'data/034_World/qa.parquet', '035_Billboard': 'data/035_Billboard/qa.parquet', '036_US': 'data/036_US/qa.parquet', '037_Ted': 'data/037_Ted/qa.parquet', '038_Stroke': 'data/038_Stroke/qa.parquet', '039_Happy': 'data/039_Happy/qa.parquet', '040_Speed': 'data/040_Speed/qa.parquet', '041_Airline': 'data/041_Airline/qa.parquet', '042_Predict': 'data/042_Predict/qa.parquet', '043_Predict': 'data/043_Predict/qa.parquet', '044_IMDb': 'data/044_IMDb/qa.parquet', '045_Predict': 'data/045_Predict/qa.parquet', '046_120': 'data/046_120/qa.parquet', '047_Bank': 'data/047_Bank/qa.parquet', '048_Data': 'data/048_Data/qa.parquet', '049_Boris': 'data/049_Boris/qa.parquet', '050_ING': 'data/050_ING/qa.parquet', '051_Pokemon': 'data/051_Pokemon/qa.parquet', '052_Professional': 'data/052_Professional/qa.parquet', '053_Patents': 'data/053_Patents/qa.parquet', '054_Joe': 'data/054_Joe/qa.parquet', '055_German': 'data/055_German/qa.parquet', '056_Emoji': 'data/056_Emoji/qa.parquet', '057_Spain': 'data/057_Spain/qa.parquet', '058_US': 'data/058_US/qa.parquet', '059_Second': 'data/059_Second/qa.parquet', '060_Bakery': 'data/060_Bakery/qa.parquet', '061_Disneyland': 'data/061_Disneyland/qa.parquet', '062_Trump': 'data/062_Trump/qa.parquet', '063_Influencers': 'data/063_Influencers/qa.parquet', '064_Clustering': 'data/064_Clustering/qa.parquet', '065_RFM': 'data/065_RFM/qa.parquet'}

MODEL_NAME = "microsoft/Phi-3.5-mini-instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Setup BitsAndBytes config for efficient model loading
bnb_config = BitsAndBytesConfig(
    load_in_8bit=True  # Using 8-bit quantization for this case
)

# Load the model with HuggingFace's `from_pretrained` function
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    quantization_config=bnb_config
)

# Create a Hugging Face pipeline object
hf_pipeline = pipeline(
    "text-generation",  # Task type
    model=model,        # Pretrained model
    tokenizer=tokenizer, # Tokenizer
    max_new_tokens=4096, # Set very high value for max_new_tokens
    max_length=4096
    # device=0            # Set device to 0 for GPU, -1 for CPU
)

# Use the Hugging Face pipeline object in the LangChain HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=hf_pipeline)

# Define a prompt template using the updated import
prompt_template = """
import pandas as pd
import numpy as np

def answer(df):
    '''
    Returns : {question}
    Return Type : {return_type}
    '''
    ''' 
    The df dtypes are:
    {dtype_dict}
    '''
    {df_filtered}
    # Your implementation goes here
    return 

df = pd.read_parquet("{df_path}")
print(answer(df))
"""

# Create the PromptTemplate object with the updated import
prompt = PromptTemplate(
    input_variables=["question", "return_type", "dtype_dict", "df_filtered", "df_path"],
    template=prompt_template
)

# Create a LangChain LLMChain with the updated import
llm_chain = LLMChain(llm=llm, prompt=prompt)


# Function to process each dataset and generate results
def process_dataset(df_q, df, df_path):
    results = {}
    for i in tqdm(range(df_q.shape[0])):
        try:
            # Extract details for the prompt
            data_row = df_q.iloc[i]
            question = data_row['question']
            cols_used = data_row['columns_used']
            col_dtypes = data_row['column_types']
            return_type = data_row['type']
            dtype_dict = dict(zip(cols_used, col_dtypes))
            df_filtered = df[cols_used]

            # Format input data for the LLMChain
            input_data = {
                "question": question,
                "return_type": return_type,
                "dtype_dict": dtype_dict,
                "df_filtered": df_filtered,
                "df_path": df_path
            }

            # Generate the function code using LangChain
            response = llm_chain.run(input_data)

            # Execute the generated code
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                exec(response)

            # Capture the result
            result = output.getvalue()
            answer = result  # Store the generated answer

            results[i] = {
                "question": question,
                "model_answer": answer,
                "sample_answer": data_row['sample_answer'],
                "answer": data_row['answer']
            }

        except Exception as e:
            print(f"Error processing row {i}: {e}")
            continue

    return results

# Process all datasets
all_results = {}

for k, v in splits_q.items():
    print(f"Processing dataset: {k}")
    df_path = "data/lite/" + f"{k}.parquet"
    df_q_path = "data/questions/" + f"{k}.parquet"

    try:
        df = pd.read_parquet(df_path)
        df_q = pd.read_parquet(df_q_path)
        results = process_dataset(df_q, df, df_path)
        all_results[k] = results

    except Exception as e:
        print(f"Error loading dataset {k}: {e}")
        continue

import pickle

# Save results to a pickle file
with open('results_phi35_code1_lite_langchain.pkl', 'wb') as f:
    pickle.dump(all_results, f)
