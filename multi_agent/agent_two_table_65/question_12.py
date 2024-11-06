import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the columns 'Description' and 'Quantity' from the dataframe
df = df[['Description', 'Quantity']]
# Sort the dataframe by 'Quantity' in descending order
df_sorted = df.sort_values(by='Quantity', ascending=False)
# Get the top 3 items with the highest quantities ordered
top_3_items = df_sorted['Description'].head(3)
# Print the result
print(top_3_items.tolist())