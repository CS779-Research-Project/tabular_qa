import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the column 'UnitPrice' from the dataframe
unit_price = df['UnitPrice']
# Calculate the average unit price
average_unit_price = unit_price.mean()
# Print the result
print(average_unit_price)