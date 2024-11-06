import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the column 'StockCode' from the dataframe
stock_codes = df['StockCode']
# Calculate the number of unique stock codes
unique_stock_codes = stock_codes.nunique()
# Print the result
print(unique_stock_codes)