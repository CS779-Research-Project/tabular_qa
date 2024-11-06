import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the columns 'author_name' and 'user_favourites_count' from the dataframe
df = df[['author_name<gx:category>', 'user_favourites_count<gx:number>']]
# Sort the dataframe by 'user_favourites_count' in descending order
df = df.sort_values(by='user_favourites_count<gx:number>', ascending=False)
# Get the top 4 authors
top_authors = df['author_name<gx:category>'].head(4).tolist()
# Print the result
print(top_authors)