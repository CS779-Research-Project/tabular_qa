import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the columns 'InvoiceNo' and 'Quantity' from the dataframe
df = df[['InvoiceNo', 'Quantity', 'StockCode']]
# Sort the dataframe by 'Quantity' in ascending order
df = df.sort_values('Quantity')
# Get the 'InvoiceNo' of the bottom 4 transactions
bottom_4_invoices = df['InvoiceNo'].head(4)
# Extract the 'StockCode' corresponding to these 'InvoiceNo' from the original dataframe
stock_codes = df[df['InvoiceNo'].isin(bottom_4_invoices)]['StockCode'].tolist()
# Print the list
print(stock_codes)