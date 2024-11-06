import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the columns 'animal_name', 'feathers', and 'legs' from the dataframe
df = df[['animal_name', 'feathers', 'legs']]
# Filter the dataframe to get animals with feathers
animals_with_feathers = df[df['feathers'] == True]
# Calculate the average number of legs among these animals
average_legs = animals_with_feathers['legs'].mean()
# Print the result
print(average_legs)