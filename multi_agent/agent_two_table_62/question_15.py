import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the column 'author_name' from the dataframe
author_name = df['author_name']
# Group the dataframe by 'author_name' and count the number of tweets for each author
tweet_count = author_name.value_counts()
# Sort the dataframe by the count in ascending order
tweet_count_sorted = tweet_count.sort_values(ascending=True)
# Get the bottom 3 author names
bottom_3_authors = tweet_count_sorted.index[:3].tolist()
# Print the result
print(bottom_3_authors)