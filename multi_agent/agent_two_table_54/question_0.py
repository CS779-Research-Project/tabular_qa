import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the columns 'author_id', 'user_followers_count', and 'user_verified' from the dataframe
df = df[['author_id', 'user_followers_count', 'user_verified']]
# Find the author(s) with the highest number of followers
highest_followers = df['user_followers_count'].max()
authors_with_highest_followers = df[df['user_followers_count'] == highest_followers]
# Check if any of the author(s) with the highest number of followers are verified
is_verified = authors_with_highest_followers['user_verified'].any()
# Print the result
print(is_verified)