import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'num_claims' from the dataframe
num_claims = df['num_claims']
# Calculate the average number of claims
average_claims = num_claims.mean()
# Print the result
print(average_claims)