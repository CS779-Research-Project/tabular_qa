import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the columns 'Loan Amount' and 'Job' from the dataframe
df = df[['Loan Amount', 'Job']]
# Group the dataframe by 'Job'
grouped = df.groupby('Job')
# Sort the groups by 'Loan Amount' in descending order
sorted_grouped = grouped.apply(lambda x: x.sort_values('Loan Amount', ascending=False))
# Get the top 3 jobs with the highest loan amount
top_3_jobs = sorted_grouped.groupby('Job').head(3)['Job'].unique().tolist()
# Print the result
print(top_3_jobs)