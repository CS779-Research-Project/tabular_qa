import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the columns 'name' and 'page_rank_norm' from the dataframe and sort by 'page_rank_norm' in ascending order
df_sorted = df[['name', 'page_rank_norm']].sort_values(by='page_rank_norm').head(2)
# Get the bottom 2 entities
bottom_2_entities = df_sorted['name'].tolist()
# Print the result
print(bottom_2_entities)