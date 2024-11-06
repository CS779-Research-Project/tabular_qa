import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the columns 'organization' and 'num_claims' from the dataframe
df = df[['organization', 'num_claims']]
# Group the dataframe by 'organization'
grouped = df.groupby('organization')
# Sum the 'num_claims' for each organization
claims_sum = grouped['num_claims'].sum()
# Find the organization with the highest sum of 'num_claims'
max_claims_organization = claims_sum.idxmax()
# Print the result
print(max_claims_organization)