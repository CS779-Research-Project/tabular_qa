import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the column 'Quantity' from the dataframe
quantity = df['Quantity']
# Calculate the maximum quantity
max_quantity = quantity.max()
# Print the result
print(max_quantity)