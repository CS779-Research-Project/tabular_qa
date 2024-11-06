import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'kind' from the dataframe
kind = df['kind']
# Get the unique values in the 'kind' column
unique_kinds = kind.unique()
# Sort the unique values in descending order based on their frequency
frequency = kind.value_counts().sort_values(ascending=False)
# Get the top 5 most frequent values
top_5_kinds = frequency.index[:5]
# Print the result
print(top_5_kinds.tolist())