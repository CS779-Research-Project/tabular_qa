import pandas as pd

# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')

# Filter out the rows where the 'Country' column is equal to 'United Kingdom'
uk_transactions = df[df['Country'] == 'United Kingdom']

# Count the number of rows in the filtered dataframe
num_uk_transactions = uk_transactions.shape[0]

# Print the result
print(num_uk_transactions)