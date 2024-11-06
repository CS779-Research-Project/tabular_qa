import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the columns 'Total Fat (g)', 'Total Sugar (g)', and 'Protein (g)' from the dataframe
df = df[['Total Fat (g)', 'Total Sugar (g)', 'Protein (g)']]
# Check if there are any foods with zero fat, no sugar, and more than 10 grams of protein
no_fat_foods = (df['Total Fat (g)'] == 0) & (df['Total Sugar (g)'] == 0) & (df['Protein (g)'] > 10)
# Print the result
print(no_fat_foods.any())