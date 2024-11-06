import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the column 'generation' from the dataframe
generation = df['generation']
# Filter the dataframe to get the third generation
third_generation = generation[generation == 3]
# Count the number of Pokémon in the third generation
count = third_generation.count()
# Print the result
print(count)