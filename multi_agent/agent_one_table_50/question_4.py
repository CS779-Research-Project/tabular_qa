import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the column 'author_name' from the dataframe
author_name = df['author_name']
# Get the unique author names
unique_authors = author_name.unique()
# Get the count of unique author names
count_unique_authors = len(unique_authors)
# Print the result
print(count_unique_authors)