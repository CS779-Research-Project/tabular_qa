import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the columns 'defense' and 'type1' from the dataframe
df = df[['defense', 'type1']]
# Find the Pokémon with the highest defense stat
highest_defense = df['defense'].max()
pokemon = df[df['defense'] == highest_defense]
# Get the primary type of the Pokémon
primary_type = pokemon['type1'].mode()[0]
# Print the result
print(primary_type)