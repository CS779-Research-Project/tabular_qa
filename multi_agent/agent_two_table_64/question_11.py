import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the columns 'animal_name' and'venomous' from the dataframe
df = df[['animal_name','venomous']]
# Get the first animal that is venomous
# Assuming venomous animals are represented by 1 in the'venomous' column
first_venomous_animal = df[df['venomous'] == 1]['animal_name'].iloc[0]
# Print the result
print(first_venomous_animal)