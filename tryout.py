from datasets import load_dataset


dev_qa = load_dataset("cardiffnlp/databench", "semeval", split="dev")
# dev_qa = load_dataset("cardiffnlp/databench", "semeval", split="train")

print(dev_qa)