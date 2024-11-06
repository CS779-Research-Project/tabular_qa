import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the column 'author_name' from the dataframe
author_name = df['author_name']
# Count the unique values in the 'author_name' column
unique_authors = author_name.nunique()
# Print the result with a clear message
print(f"The number of unique authors is: {unique_authors}")