import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the column 'Transaction' from the dataframe
transactions = df['Transaction']
# Check if all values in the 'Transaction' column are unique
unique_transactions = transactions.is_unique
# Convert the result to a boolean value
is_unique = unique_transactions.bool()
# Print the result
print(is_unique)