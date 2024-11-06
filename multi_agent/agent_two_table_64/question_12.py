import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the columns 'animal_name' and 'legs' from the dataframe
df = df[['animal_name', 'legs']]
# Sort the dataframe by 'legs' in descending order
df = df.sort_values('legs', ascending=False)
# Get the top 3 animal names
top_3_animals = df['animal_name'].head(3)
# If there are more than two animals with the same number of legs, sort them alphabetically
if len(top_3_animals) > 2:
    # Create a mask for animals with the same number of legs
    same_legs_mask = df['legs'].isin(df['legs'].iloc[:3])
    # Sort the animals with the same number of legs alphabetically
    top_3_animals = top_3_animals[same_legs_mask].sort_values()
# Print the result
print(top_3_animals.tolist())