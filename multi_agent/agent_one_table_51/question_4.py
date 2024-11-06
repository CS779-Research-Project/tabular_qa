import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Group the dataframe by 'generation'
grouped = df.groupby('generation')
# Count the number of Pokémon in each generation
counts = grouped.size()
# Print the result
print(counts)