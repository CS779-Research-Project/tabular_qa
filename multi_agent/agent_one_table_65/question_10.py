import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Select the relevant columns 'Description' and 'Quantity'
df = df[['Description', 'Quantity']]
# Find the item with the highest quantity ordered
highest_quantity_item = df[df['Quantity'] == df['Quantity'].max()]
# Extract the description of the item
description = highest_quantity_item['Description'].iloc[0]
# Print the result
print(description)