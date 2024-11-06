import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the column 'total' from the dataframe
total = df['total']
# Check if there are any values greater than 700
result = total > 700
# Print the result
print(result.any())