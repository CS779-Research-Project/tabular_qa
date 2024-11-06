import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the 'Transaction' column from the DataFrame
transactions = df['Transaction']
# Count the frequency of each unique transaction value
transaction_counts = transactions.value_counts()
# Get the indices of the top 5 most frequent transactions
top_5_transaction_indices = transaction_counts.head(5).index
# Convert these indices to a list of numbers
top_5_transactions = top_5_transaction_indices.tolist()
# Print the list of top 5 transaction numbers by frequency
print(top_5_transactions)