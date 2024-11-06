import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the columns 'author_name<gx:category>' and 'user_followers_count<gx:number>' from the dataframe
df = df[['author_name<gx:category>', 'user_followers_count<gx:number>']]
# Sort the dataframe by 'user_followers_count<gx:number>' in descending order
df = df.sort_values(by='user_followers_count<gx:number>', ascending=False)
# Get the top 3 authors
top_3_authors = df['author_name<gx:category>'].head(3).tolist()
# Print the result
print(top_3_authors)