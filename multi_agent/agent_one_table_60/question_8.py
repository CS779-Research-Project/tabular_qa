import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'period_day' and 'Transaction' from the dataframe
df = df[['period_day', 'Transaction']]
# Group the dataframe by 'period_day'
grouped_df = df.groupby('period_day')
# Count the number of transactions for each period
transaction_counts = grouped_df['Transaction'].count()
# Find the period with the highest number of transactions
highest_transaction_period = transaction_counts.idxmax()
# Print the result
print(highest_transaction_period)