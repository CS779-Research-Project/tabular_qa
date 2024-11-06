import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns'retweets' and 'favorites' from the dataframe
df = df[['retweets', 'favorites']]
# Sort the dataframe by 'favorites' in descending order
df = df.sort_values('favorites', ascending=False)
# Select the top 5 rows
top_5_posts = df.head(5)
# Extract the'retweets' column from the selected rows
retweets = top_5_posts['retweets']
# Convert the extracted column to a list
retweets_list = retweets.tolist()
# Print the result
print(retweets_list)