import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the column 'Transaction' from the dataframe
transaction = df['Transaction']
# Find the highest transaction number
highest_transaction = transaction.max()
# Print the result
print(highest_transaction)