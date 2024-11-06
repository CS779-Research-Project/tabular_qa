import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the column 'total' from the dataframe
total_stats = df['total']
# Calculate the highest total stat value
highest_total_stat = total_stats.max()
# Print the result
print(highest_total_stat)