import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the columns 'author_name' and'retweets' from the dataframe
df = df[['author_name<gx:category>','retweets<gx:number>']]
# Sort the dataframe by'retweets' in descending order
df = df.sort_values('retweets<gx:number>', ascending=False)
# Get the top 2 authors
top_2_authors = df['author_name<gx:category>'].head(2).tolist()
# Print the result
print(top_2_authors)