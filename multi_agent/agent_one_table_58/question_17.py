import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'Weight' from the dataframe
weights = df['Weight']
# Get the unique weight values
unique_weights = weights.unique()
# Get the highest 4 unique weight values
highest_weights = unique_weights[unique_weights.argsort()[-4:][::-1]]
# Print the result
print(highest_weights)