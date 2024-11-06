import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter the dataframe for legendary Pokémon
legendary_df = df[df['legendary'] == True]
# Calculate the average speed of the legendary Pokémon
average_speed = legendary_df['speed'].mean()
# Print the result
print(average_speed)