import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Count the number of rows where'mention_ids' is an empty list
no_mentions = df[df['mention_ids'].apply(lambda x: len(x) == 0)].shape[0]
# Print the result
print(no_mentions)