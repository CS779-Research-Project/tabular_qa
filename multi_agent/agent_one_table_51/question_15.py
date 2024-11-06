import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the columns 'generation', 'attack', and 'name' from the dataframe
df = df[['generation', 'attack', 'name']]
# Filter the dataframe to get the second generation Pokémon
second_generation = df[df['generation'] == 2]
# Sort the filtered dataframe by 'attack' in descending order
sorted_df = second_generation.sort_values('attack', ascending=False)
# Get the top 6 Pokémon from the sorted dataframe
top_6_pokemon = sorted_df.head(6)
# Extract the 'name' column from the top 6 Pokémon
names = top_60_pokemon['name']
# Print the result as a list
print(names.tolist())