import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter the dataframe to get the transactions made during the afternoon
afternoon_transactions = df[df['period_day'] == 'afternoon']
# Count the number of unique transactions
count = afternoon_transactions['Transaction'].nunique()
# Print the result
print(count)