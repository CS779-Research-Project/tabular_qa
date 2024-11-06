import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the column 'generation' and'speed' from the dataframe
df = df[['generation','speed']]
# Filter the dataframe to get the fourth generation
fourth_generation = df[df['generation'] == 4]
# Sort the dataframe by'speed' in descending order
fourth_generation_sorted = fourth_generation.sort_values('speed', ascending=False)
# Get the top 4 rows
top_4_speed = fourth_generation_sorted.head(4)
# Extract the'speed' values into a list
top_4_speeds = top_4_speed['speed'].tolist()
# Print the result
print(top_4_speeds)