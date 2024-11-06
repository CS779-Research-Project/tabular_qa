import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the column 'Self-transcendence' from the dataframe
self_transcendence = df['Self-transcendence']
# Sort the self_transcendence column in ascending order
sorted_self_transcendence = self_transcendence.sort_values()
# Get the lowest 6 levels of Self-transcendence
lowest_six_levels = sorted_self_transcendence[:6]
# Print the result
print(lowest_six_levels.tolist())