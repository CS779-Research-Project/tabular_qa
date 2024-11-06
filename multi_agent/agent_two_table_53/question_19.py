import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the columns 'id' and 'date' from the dataframe
df = df[['id', 'date']]
# Sort the dataframe by 'date' in descending order
df = df.sort_values(by='date', ascending=False)
# Get the top 6 rows
top_6_patents = df.head(6)
# Extract the 'id' column from the top 6 rows
patent_ids = top_6_patents['id'].tolist()
# Print the result
print(patent_ids)