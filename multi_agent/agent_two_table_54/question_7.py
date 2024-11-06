import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the column'mention_names' from the dataframe
mention_names = df['mention_names']
# Count the number of unique mentions
unique_mentions = mention_names.nunique()
# Print the result
print(unique_mentions)