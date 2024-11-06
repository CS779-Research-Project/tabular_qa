import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column'model' from the dataframe
models = df['model']
# Filter the dataframe with the column'model' to only include 'Golf'
golf_models = df[models == 'Golf']
# Filter the dataframe with the column'price'
prices = golf_models['price']
# Calculate the average price
average_price = prices.mean()
# Print the result
print(average_price)