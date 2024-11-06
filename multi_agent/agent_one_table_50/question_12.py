import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns 'author_name' and'retweets' from the dataframe
df = df[['author_name','retweets']]
# Sort the dataframe by'retweets' in descending order
df = df.sort_values('retweets', ascending=False)
# Get the top 3 rows
top_3 = df.head(3)
# Extract the 'author_name' from these rows
top_3_authors = top_3['author_name'].tolist()
# Print the list
print(top_3_authors)