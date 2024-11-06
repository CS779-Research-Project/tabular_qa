import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Select the column 'Self-transcendence' from the dataframe
self_transcendence = df['Self-transcendence']
# Calculate the minimum value of the 'Self-transcendence' column
min_self_transcendence = self_transcendence.min()
# Print the minimum value of 'Self-transcendence'
print(min_self_transcendence)