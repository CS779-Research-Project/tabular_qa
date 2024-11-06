import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the columns 'Description' and 'Quantity' from the dataframe
df = df[['Description', 'Quantity']]
# Sort the dataframe by 'Quantity' in ascending order
df = df.sort_values(by='Quantity')
# In case of a tie, sort the tied items by 'Description' in alphabetical order
df = df.sort_values(by=['Quantity', 'Description'])
# Get the descriptions of the first 2 items
lowest_quantities = df['Description'].head(2)
# Print the result
print(lowest_quantities.tolist())