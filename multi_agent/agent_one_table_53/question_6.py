import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'num_claims' from the dataframe
num_claims = df['num_claims']
# Find the maximum value in the 'num_claims' column
max_claims = num_claims.max()
# Print the result
print(max_claims)