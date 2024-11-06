import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the column 'is_organization' from the dataframe
is_organization = df['is_organization']
# Check if there are any True values in the filtered column
individuals_exist = is_organization.any()
# Print the result
print(individuals_exist)