import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the column 'type' from the dataframe
type_column = df['type']
# Get the unique values in the 'type' column
unique_types = type_column.unique()
# Get the frequency of each unique value
type_counts = type_column.value_counts()
# Sort the unique values in descending order based on their frequency
sorted_types = type_counts.index.tolist()
sorted_types.sort(key=lambda x: type_counts[x], reverse=True)
# Get the top 6 most common types
top_6_types = sorted_types[:6]
# Print the result
print(top_6_types.tolist())