import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the columns 'Loan Duration - Months' and 'Job' from the dataframe
df = df[['Loan Duration - Months', 'Job']]
# Get the top 4 unique jobs
top_jobs = df['Job'].value_counts().index[:4].tolist()
# Print the result
print(top_jobs)