import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter and sort the dataframe in one step
fourth_generation_sorted = df[df['generation'] == 4].sort_values('speed', ascending=False).head(4)[['speed']].values.flatten().tolist()
# Print the result
print(fourth_generation_sorted)