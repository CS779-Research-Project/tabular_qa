import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Select the relevant columns 'Country' and 'CustomerID'
df = df[['Country', 'CustomerID']]
# Find the customer with the lowest 'CustomerID'
lowest_customer_id = df['CustomerID'].min()
# Extract the 'Country' value for that customer
country = df[df['CustomerID'] == lowest_customer_id]['Country'].values[0]
# Print the result
print(country)