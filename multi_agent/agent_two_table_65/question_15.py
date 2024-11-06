import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Group the dataframe by 'Country' and count the number of transactions
transaction_counts = df['Country'].value_counts()
# Get the countries with the least transactions
least_transactions_countries = transaction_counts.nsmallest(2).index.tolist()
# Print the result
print(least_transactions_countries)