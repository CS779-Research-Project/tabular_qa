import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the columns 'id' and 'page_rank_norm' from the dataframe
df = df[['id', 'page_rank_norm']]
# Sort the dataframe by 'page_rank_norm' in ascending order
df_sorted = df.sort_values(by='page_rank_norm')
# Get the bottom 4 'id' values
bottom_4_ids = df_sorted['id'].head(4).tolist()
# Print the result
print(bottom_4_ids)