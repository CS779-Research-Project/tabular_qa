import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column 'price' from the dataframe
price = df['price']
# Find the highest price
highest_price = price.max()
# Print the result
print(highest_price)