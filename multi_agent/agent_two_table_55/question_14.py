import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the columns 'Number of Existing Loans' and 'Job' from the dataframe
df = df[['Number of Existing Loans', 'Job']]
# Group the dataframe by 'Job'
grouped = df.groupby('Job')
# Get the index of the maximum 'Number of Existing Loans'
max_loans_index = grouped['Number of Existing Loans'].idxmax()
# Filter the groups to get the groups with the maximum 'Number of Existing Loans'
max_loans_jobs = grouped.get_group(max_loans_index)
# Get the 'Job' values from the filtered groups
jobs = max_loans_jobs['Job'].unique()
# Print the result
print(jobs)