import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns 'author_name' and'retweets' from the dataframe
df = df[['author_name','retweets']]
# Group the dataframe by 'author_name' with observed=False
grouped = df.groupby('author_name', observed=False)
# Check if any author has a retweet count of 0
no_retweets = grouped['retweets'].sum() == 0
# Print the result
print(no_retweets.any())