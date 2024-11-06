import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'Weight' from the dataframe
weights = df['Weight']
# Get the unique weight values
unique_weights = weights.unique()
# Sort the unique weight values in descending order
sorted_weights = unique_weights[unique_weights.argsort()[::-1]]
# Get the highest 4 unique weight values
highest_weights = sorted_weights[:4]
# Print the result
print(highest_weights)