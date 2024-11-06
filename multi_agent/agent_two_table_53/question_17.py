import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the columns 'id' and 'num_claims' from the dataframe
df = df[['id', 'num_claims']]
# Sort the dataframe by 'num_claims' in descending order
df = df.sort_values('num_claims', ascending=False)
# Get the top 3 rows
top_3 = df.head(3)
# Extract the 'id' column from these rows
ids = top_3['id'].tolist()
# Print the result
print(ids)