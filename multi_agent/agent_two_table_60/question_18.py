import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'Transaction' and 'Item' from the dataframe
df = df[['Transaction', 'Item']]
# Filter the dataframe to get the transactions where 'Bread' was purchased
bread_transactions = df[df['Item'] == 'Bread']
# Get the top 6 transaction numbers
top_6_transactions = bread_transactions['Transaction'].nlargest(6).tolist()
# Print the result
print(top_6_transactions)