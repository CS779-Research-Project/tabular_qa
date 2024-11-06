import pandas as pd

# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')

# Filter out the 'weight' column from the DataFrame
weight = df['weight']

# Calculate the maximum weight
max_weight = weight.max()

# Print the result
print(max_weight)