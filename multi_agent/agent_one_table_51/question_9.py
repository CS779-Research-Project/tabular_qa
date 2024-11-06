import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the columns'speed' and 'name' from the dataframe
df = df[['speed', 'name']]
# Find the minimum speed value
min_speed = df['speed'].min()
# Get the name of the Pokémon with the minimum speed
pokemon_name = df[df['speed'] == min_speed]['name'].values[0]
# Print the result
print(pokemon_name)