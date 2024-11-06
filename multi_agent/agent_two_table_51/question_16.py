import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the column'sp_defense' from the dataframe
sp_defense = df['sp_defense']
# Sort the dataframe by'sp_defense' in descending order
sp_defense_sorted = sp_defense.sort_values(ascending=False)
# Get the top 5 values
top_5_sp_defense = sp_defense_sorted.head(5)
# Convert the result to a list
top_5_sp_defense_list = top_5_sp_defense.tolist()
# Print the result
print(top_5_sp_defense_list)