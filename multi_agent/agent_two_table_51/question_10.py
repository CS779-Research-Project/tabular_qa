import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the columns 'legendary' and 'type2' from the dataframe
df = df[['legendary', 'type2']]
# Filter the dataframe to get only legendary Pokémon and count the frequency of each unique value in 'type2'
type2_counts = df[df['legendary'] == True]['type2'].value_counts()
# Find the most common value
most_common_type2 = type2_counts.idxmax()
# Print the result
print(most_common_type2)