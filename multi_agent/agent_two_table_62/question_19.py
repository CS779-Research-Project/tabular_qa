import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the column'retweets' from the dataframe
retweets = df['retweets']
# Sort the dataframe by'retweets' in descending order
sorted_retweets = retweets.sort_values(ascending=False)
# Get the bottom 3 retweet counts
bottom_3_retweets = sorted_retweets.head(3)
# Print the result
print(bottom_3_retweets.tolist())