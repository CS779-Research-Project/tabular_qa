import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the columns 'Age' and 'Job' from the dataframe
df = df[['Age', 'Job']]
# Sort the dataframe by 'Age' in ascending order
df = df.sort_values(by='Age')
# Get the top 2 oldest borrowers
top_2_oldest = df.head(2)
# Get their jobs
jobs = top_2_oldest['Job'].tolist()
# Print the result
print(jobs)