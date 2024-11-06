import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'type' from the dataframe
type_column = df['type']
# Count the frequency of each unique value in the 'type' column
type_counts = type_column.value_counts()
# Sort the frequency count in descending order
type_counts_sorted = type_counts.sort_values(ascending=False)
# Get the top 4 most common types
top_4_types = type_counts_sorted[:4].index.tolist()
# Print the result
print(top_4_types)