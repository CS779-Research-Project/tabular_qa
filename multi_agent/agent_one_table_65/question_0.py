import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the column 'Quantity' from the dataframe
quantity = df['Quantity']
# Check if all values in the 'Quantity' column are greater than 0
all_greater_than_zero = quantity > 0
# Print the result
print(all_greater_than_zero.all())