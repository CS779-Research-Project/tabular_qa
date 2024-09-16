from datasets import load_dataset


dev_qa = load_dataset("cardiffnlp/databench", "semeval", split="dev")

print(dev_qa)