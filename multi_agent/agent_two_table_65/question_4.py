import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Calculate the number of unique stock codes
unique_stock_codes = df['StockCode'].nunique()
# Print the result
print(unique_stock_codes)