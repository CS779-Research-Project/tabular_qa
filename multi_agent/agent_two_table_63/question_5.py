import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the column 'page_rank_norm' from the dataframe
page_rank_norm = df['page_rank_norm']
# Calculate the average page rank norm
average_page_rank_norm = page_rank_norm.mean()
# Print the result
print(f"The average page rank norm is: {average_page_rank_norm:.2f}")