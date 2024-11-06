import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'organization' from the dataframe
organizations = df['organization']
# Count the unique organizations
unique_organizations = organizations.nunique()
# Print the result
print(unique_organizations)