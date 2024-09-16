# from datasets import load_dataset

# Load all QA pairs
# all_qa = load_dataset("cardiffnlp/databench", name="qa", split="full")

# # Load SemEval 2025 task 8 Question-Answer splits
# semeval_train_qa = load_dataset("cardiffnlp/databench", name="semeval", split="train")
# semeval_dev_qa = load_dataset("cardiffnlp/databench", name="semeval", split="dev")


# # "001_Forbes", the id of the dataset where information to answer the Question is located
# all_qa['dataset'][0] 

# # This id can be used load a specific Question-Answer pair collection from the splits
# forbes_qa = load_dataset("cardiffnlp/databench", name="qa", split=all_qa['dataset'][0] )

# # you can load a specific dataset containg the "answer" for a QA pair using the 
# forbes_full = load_dataset("cardiffnlp/databench", name=all_qa['dataset'][0] , split="full")

# # or to load the databench lite equivalent dataset, to answer the "sample_answer"
# forbes_sample = load_dataset("cardiffnlp/databench", name=all_qa['dataset'][0] , split="lite")

# Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
# model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-13b-chat-hf")
# model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-13b-chat-hf")