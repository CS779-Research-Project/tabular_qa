import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Select the 'author_name' and 'user_followers_count' columns
df = df[['author_name', 'user_followers_count']]
# Group the dataframe by 'author_name'
grouped_df = df.groupby('author_name')
# Find the author with the maximum 'user_followers_count'
max_followers_author = grouped_df['user_followers_count'].idxmax()
# Print the author's name
print(max_followers_author)