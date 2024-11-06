import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the'retweets' column from the dataframe
retweets = df['retweets']
# Sort the dataframe by'retweets' in descending order
sorted_retweets = retweets.sort_values(ascending=False)
# Get the top 2 rows
top_2_retweets = sorted_retweets.head(2)
# Extract the'retweets' values from these rows
top_2_retweets_values = top_2_retweets.tolist()
# Print the result
print(top_2_retweets_values)