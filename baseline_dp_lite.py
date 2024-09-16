import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
import bitsandbytes as bnb
from tqdm import tqdm

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
            cols_used = df_q.iloc[i]['columns_used']
            df_filtered = df[cols_used]
            table_data_text = df_filtered.to_csv(index=False)
            question = row['question']
            answer_format = "Answer : <" + row['type'] + ">"
            prompt = f"""
    You are an advanced AI capable of analyzing and understanding information within tables. Read the table below regarding \"{title}\"
    {table_data_text}

    Based on the given table, answer the following question : 

    {question}

    Let's think step by step, and then give the final answer. Ensure the final answer format is only \"{answer_format}\" form, no other form. And ensure the final answer is a number or entity names, as short as possible, without any explanation.
    """

            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
            generate_ids = model.generate(inputs.input_ids, max_new_tokens=150)

            # Decode the output
            response = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

            # parse out the answer, take the last instance of "Answer : "
            lines_with_answer = [line.split("Answer : ")[-1].strip() 
                        for line in response.splitlines() if "Answer : " in line]

            # Take the second occurrence if available
            answer = lines_with_answer[1] if len(lines_with_answer) > 1 else None
            results[k][i] = answer

            # print("model output : ", answer)
            # print("actual output : ", df_q.iloc[i]['answer'])
            # print("sample actual output : ", df_q.iloc[i]['sample_answer'])
            # assert False
            results[k][i] = {"question": question, "model_answer": answer, "sample_answer" : row['sample_answer'], "answer": row['answer']}
    except Exception as e:
        print(e)
        continue

import pickle

with open('phi35_dp_lite.pkl', 'wb') as f:
    pickle.dump(results, f)