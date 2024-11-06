import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the columns 'Total Fat (g)' and 'name' from the dataframe
df = df[['Total Fat (g)', 'name']]
# Find the food with the least amount of total fat
food_with_least_fat = df[df['Total Fat (g)'] == df['Total Fat (g)'].min()]
# Print the name of the food and the amount of total fat
print(f"The food with the least amount of total fat is {food_with_least_fat.iloc[0]['name']} with {food_with_least_fat.iloc[0]['Total Fat (g)']}g of total fat.")