import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'Transaction' and 'period_day' from the dataframe
transactions = df[['Transaction', 'period_day']]
# Filter the dataframe to get the transactions made during the afternoon
afternoon_transactions = transactions[transactions['period_day'] == 'afternoon']
# Count the number of transactions
count = afternoon_transactions['Transaction'].nunique()
# Print the result
print(count)