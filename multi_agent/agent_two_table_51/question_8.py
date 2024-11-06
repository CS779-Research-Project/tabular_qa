import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Find the Pokémon with the highest defense stat
index_highest_defense = df['defense'].idxmax()
pokemon = df.loc[index_highest_defense]
# Get the primary type of the Pokémon
primary_type = pokemon['type1'].mode()[0]
# Print the result
print(primary_type)