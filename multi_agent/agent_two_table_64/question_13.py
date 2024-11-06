import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the columns 'animal_name' and 'legs' from the dataframe
df = df[['animal_name', 'legs']]
# Sort the dataframe by 'legs' in ascending order
df = df.sort_values('legs')
# Get the bottom 2 animal names
bottom_2_animals = df['animal_name'].head(2)
# If there are more than two with the lowest number, sort these animals alphabetically
if len(bottom_2_animals) > 2:
    bottom_2_animals = bottom_2_animals.sort_values().tolist()
else:
    bottom_2_animals = bottom_2_animals.tolist()
# Print the result
print(bottom_2_animals)