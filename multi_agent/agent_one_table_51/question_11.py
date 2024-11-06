import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the columns'sp_attack', 'name', and 'type1' from the dataframe
df = df[['sp_attack', 'name', 'type1']]
# Find the Pokémon with the highest special attack
highest_sp_attack = df['sp_attack'].max()
pokemon = df[df['sp_attack'] == highest_sp_attack]
# Get the name and primary type of the Pokémon
name = pokemon['name']
primary_type = pokemon['type1']
# Print the result
print(f"The Pokémon with the highest special attack is {name.values[0]} and its primary type is {primary_type.values[0]}")