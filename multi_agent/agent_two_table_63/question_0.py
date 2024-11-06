import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the rows where 'community' is 'Tech', 'page_rank_norm' is greater than 0.5, and 'twitter_profile_id' is not None (or not False)
filtered_df = df[(df['community'] == 'Tech') & (df['page_rank_norm'] > 0.5) & (df['twitter_profile_id'].notnull())]
# Calculate the average weight of the filtered influencers
average_weight = filtered_df['weight'].mean()
# Print the result
print(average_weight)