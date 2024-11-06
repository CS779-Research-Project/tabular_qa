import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the column'mention_ids' from the dataframe
mention_ids = df['mention_ids']
# Count the number of rows where'mention_ids' is an empty list
no_mentions = mention_ids[mention_ids.apply(lambda x: len(x) == 0)].count()
# Print the result
print(no_mentions)