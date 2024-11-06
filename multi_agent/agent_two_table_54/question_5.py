import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter the dataframe to get the rows where 'user_favourites_count' is greater than 10,000
df_filtered = df[df['user_favourites_count'] > 10000]
# Count the number of unique authors in the filtered dataframe
num_authors = df_filtered['author_id'].nunique()
# Print the result
print(num_authors)