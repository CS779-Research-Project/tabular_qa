import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'kind' from the dataframe
kind = df['kind']
# Count the frequency of each unique value in the 'kind' column
kind_counts = kind.value_counts()
# Find the most common value
most_common_kind = kind_counts.idxmax()
# Print the result
print(f"The most common kind is '{most_common_kind}' with a count of {kind_counts[most_common_kind]}")