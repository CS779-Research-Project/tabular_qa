import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'Transaction' and 'period_day' from the dataframe
df = df[['Transaction', 'period_day']]
# Filter the dataframe to get the transactions made in the morning
morning_transactions = df[df['period_day'] =='morning']
# Get the bottom 2 transaction numbers
bottom_2_transactions = morning_transactions['Transaction'].nsmallest(2).tolist()
# Print the result
print(bottom_2_transactions)