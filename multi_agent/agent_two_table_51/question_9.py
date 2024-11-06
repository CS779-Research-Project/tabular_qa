import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the columns'speed' and 'name' from the dataframe
df = df[['speed', 'name']]
# Find the index of the minimum speed value
min_speed_index = df['speed'].idxmin()
# Get the name of the Pokémon with the minimum speed
pokemon_name = df.loc[min_speed_index, 'name']
# Print the result
print(pokemon_name)