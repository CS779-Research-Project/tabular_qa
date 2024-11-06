import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the column 'user_followers_count' from the dataframe
followers_count = df['user_followers_count']
# Sort the filtered dataframe in descending order based on 'user_followers_count'
sorted_followers_count = followers_count.sort_values(ascending=False)
# Get the top 3 values
top_3_followers_count = sorted_followers_count.head(3)
# Print the result
print(top_3_followers_count.tolist())