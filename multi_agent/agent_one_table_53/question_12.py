import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'organization' from the dataframe
organizations = df['organization']
# Group the dataframe by 'organization'
grouped = organizations.groupby(organizations)
# Count the number of patents for each organization
counts = grouped.count()
# Sort the organizations by the number of patents in descending order
sorted_counts = counts.sort_values(ascending=False)
# Get the top 3 organizations
top_3_organizations = sorted_counts.index[:3]
# Print the result
print(top_3_organizations.tolist())