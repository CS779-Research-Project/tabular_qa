import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the columns 'dealer' and 'price' from the dataframe
df = df[['dealer', 'price']]
# Find the dealer with the highest price
highest_price_dealer = df[df['price'] == df['price'].max()]['dealer']
# Print the result
print(highest_price_dealer)