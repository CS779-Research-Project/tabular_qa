import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the column 'Country' from the dataframe
countries = df['Country']
# Group the dataframe by 'Country' and count the number of transactions
transaction_counts = countries.value_counts()
# Get the countries with the least transactions
least_transactions_count = transaction_counts.min()
least_transactions_countries = transaction_counts[transaction_counts == least_transactions_count].index.tolist()
# Print the result
print(least_transactions_countries)