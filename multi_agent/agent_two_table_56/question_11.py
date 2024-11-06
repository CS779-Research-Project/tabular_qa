import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the columns 'Protein (g)' and 'name' from the dataframe
df = df[['Protein (g)', 'name']]
# Find the food with the highest amount of protein
index_of_highest_protein = df['Protein (g)'].idxmax()
food = df.loc[index_of_highest_protein, 'name']
# Print the name of the food
print(food)