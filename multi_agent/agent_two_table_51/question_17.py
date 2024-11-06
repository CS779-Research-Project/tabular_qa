import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the columns 'legendary' and 'defense' from the dataframe
df = df[['legendary', 'defense']]
# Sort the dataframe by 'defense' in descending order
df_sorted = df.sort_values(by='defense', ascending=False)
# Get the first 3 rows of the sorted dataframe
top_3_defense = df_sorted.head(3)
# Extract the 'defense' values from these rows
bottom_3_defense = top_3_defense['defense'].tolist()
# Print the result
print(bottom_3_defense)