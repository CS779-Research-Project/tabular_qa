import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the columns 'Description' and 'UnitPrice' from the DataFrame
df = df[['Description', 'UnitPrice']]
# Find the row with the highest 'UnitPrice'
highest_unit_price_row = df[df['UnitPrice'] == df['UnitPrice'].max()]
# Extract the 'Description' value from that row
item_description = highest_unit_price_row['Description'].values[0]
# Print the 'Description' value
print(item_description)