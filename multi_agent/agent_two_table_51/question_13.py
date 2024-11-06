import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the columns 'hp' and 'name' from the dataframe
df = df[['hp', 'name']]
# Sort the dataframe by 'hp' in descending order
df = df.sort_values(by='hp', ascending=False)
# Get the first 5 rows of the sorted dataframe
top_5_pokemon = df.head(5)
# Extract the 'name' column from these rows
names = top_5_pokemon['name']
# Convert the result to a list
names_list = names.tolist()
# Print the result
print(names_list)