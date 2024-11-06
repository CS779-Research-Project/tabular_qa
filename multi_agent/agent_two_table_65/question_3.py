import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Convert the 'InvoiceDate' column to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# Convert the 'UnitPrice' column to float
df['UnitPrice'] = df['UnitPrice'].astype(float)
# Filter the dataframe to get the transactions in December 2020
december_transactions = df[df['InvoiceDate'].dt.month == 12 & df['InvoiceDate'].dt.year == 2020]
# Calculate the total revenue by multiplying 'Quantity' and 'UnitPrice'
december_transactions['TotalRevenue'] = december_transactions['Quantity'] * december_transactions['UnitPrice']
# Sum the total revenue
total_revenue = december_transactions['TotalRevenue'].sum()
# Print the result
print(total_revenue)