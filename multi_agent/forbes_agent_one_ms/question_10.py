import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'finalWorth' and 'category' from the dataframe
df = df[['finalWorth', 'category']]
# Find the row with the highest 'finalWorth'
richest_billionaire = df['finalWorth'].idxmax()
# Get the 'category' of the richest billionaire
category = df.loc[richest_billionaire, 'category']
# Print the result
print(category)