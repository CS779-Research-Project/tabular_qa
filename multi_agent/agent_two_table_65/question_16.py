import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the columns 'InvoiceNo' and 'Quantity' from the dataframe
df = df[['InvoiceNo', 'Quantity']]
# Sort the dataframe by 'Quantity' in descending order
df = df.sort_values(by='Quantity', ascending=False)
# Get the top 5 invoice numbers
top_5_invoices = df['InvoiceNo'].head(5).tolist()
# Print the result
print(top_5_invoices)