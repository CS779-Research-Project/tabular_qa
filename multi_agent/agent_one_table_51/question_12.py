import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the columns 'total' and 'name' from the dataframe
df = df[['total', 'name']]
# Sort the dataframe by 'total' in descending order
df = df.sort_values('total', ascending=False)
# Get the top 3 rows
top_3_pokemon = df.head(3)
# Extract the 'name' column from these rows
names = top_3_pokemon['name']
# Convert the result to a list
names_list = names.tolist()
# Print the result
print(names_list)