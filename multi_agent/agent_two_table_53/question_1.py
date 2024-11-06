import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'organization' from the dataframe
organization = df['organization']
# Check if 'IBM' is present in the filtered column
ibm_present = organization.isin(['IBM']).any()
# Print the result
print(ibm_present)