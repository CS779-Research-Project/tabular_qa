import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the column 'author_name' from the dataframe
author_name = df['author_name']
# Count the frequency of each author name
author_count = author_name.value_counts()
# Find the author name with the highest frequency
most_common_author = author_count.idxmax()
# Print the result
print(most_common_author)