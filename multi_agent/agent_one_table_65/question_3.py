import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Convert the 'InvoiceDate' column to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# Filter the dataframe to get the transactions in December 2020
december_transactions = df[df['InvoiceDate'].dt.month == 12 & df['InvoiceDate'].dt.year == 2020]
# Count the number of transactions
transaction_count = december_transactions.shape[0]
# Print the result
print(transaction_count)