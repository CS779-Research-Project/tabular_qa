import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Sort the dataframe by 'total' in descending order and get the top 3 rows
top_3_pokemon = df.sort_values('total', ascending=False).head(3)[['name']]
# Convert the result to a list
names_list = top_3_pokemon['name'].tolist()
# Print the result
print(names_list)