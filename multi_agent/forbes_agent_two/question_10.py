import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'finalWorth'
df = df[df['finalWorth'] == df['finalWorth'].max()]
# Convert the 'category' column to an ordered categorical type
df['category'] = df['category'].astype('category').as_ordered()
# Get the category of the billionaire with the highest finalWorth
billionaire = df['category'].max()
# Assign the category of the richest billionaire to a variable
category = billionaire
# Print the result
print(category)