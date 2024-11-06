import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the column 'Item' from the dataframe
items = df['Item']
# Count the unique items
unique_items_count = items.nunique()
# Print the result
print(unique_items_count)