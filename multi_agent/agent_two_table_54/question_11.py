import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the columns 'author_name' and'retweets' from the dataframe
df = df[['author_name<gx:category>','retweets<gx:number>']]
# Find the tweet with the maximum number of retweets
max_retweets = df['retweets<gx:number>'].max()
tweet = df[df['retweets<gx:number>'] == max_retweets]
# Get the author name of the tweet
author_name = tweet['author_name<gx:category>'].values[0]
# Print the result
print(author_name)