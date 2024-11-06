import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns 'author_name' and'retweets' from the dataframe
df = df[['author_name','retweets']]
# Group the dataframe by 'author_name'
grouped_df = df.groupby('author_name')
# Sum the'retweets' for each author
sum_retweets = grouped_df['retweets'].sum()
# Sort the grouped dataframe by'retweets' in descending order
sorted_df = sum_retweets.sort_values(ascending=False)
# Get the name of the author with the highest number of retweets
most_retweeted_author = sorted_df.index[0]
# Print the result
print(most_retweeted_author)