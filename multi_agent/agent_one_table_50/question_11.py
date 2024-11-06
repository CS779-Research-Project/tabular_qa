import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the column 'type' from the dataframe
type_column = df['type']
# Count the frequency of each unique value in the 'type' column
type_counts = type_column.value_counts()
# Find the most common value
most_common_type = type_counts.idxmax()
# Print the result
print(most_common_type)