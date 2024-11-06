import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the column 'Country' from the dataframe
countries = df['Country']
# Count the number of transactions for each country
country_counts = countries.value_counts()
# Get the country with the most transactions
most_transactions_country = country_counts.idxmax()
# Print the result
print(most_transactions_country)