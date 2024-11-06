import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the column 'Transaction' from the dataframe
transactions = df['Transaction']
# Group the dataframe by 'Transaction'
grouped = transactions.groupby(transactions)
# Count the number of items in each transaction
counts = grouped.count()
# Sort the transactions by the count in descending order
sorted_counts = counts.sort_values(ascending=False)
# Get the top 4 transactions
top_transactions = sorted_counts.head(4)
# Print the result
print(top_transactions.index.tolist())