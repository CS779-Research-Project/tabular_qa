import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the columns 'id' and 'favorites' from the dataframe
df = df[['id', 'favorites']]
# Sort the dataframe in ascending order based on 'favorites'
df = df.sort_values(by='favorites')
# Get the bottom 4 rows
bottom_four = df.head(4)
# Extract the 'id' column from these rows
tweet_ids = bottom_four['id'].tolist()
# Print the result
print(tweet_ids)