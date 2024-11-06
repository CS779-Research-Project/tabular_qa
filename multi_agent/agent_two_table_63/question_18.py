import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the column 'page_rank_norm' from the dataframe
page_rank_norm = df['page_rank_norm']
# Sort the dataframe by 'page_rank_norm' in descending order
sorted_page_rank_norm = page_rank_norm.sort_values(ascending=False)
# Get the top 6 values
top_6_page_rank_norm = sorted_page_rank_norm.head(6)
# Convert the result to a list
top_6_page_rank_norm_list = top_6_page_rank_norm.tolist()
# Print the result
print(top_6_page_rank_norm_list)