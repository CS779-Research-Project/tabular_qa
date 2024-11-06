import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the columns 'id' and 'target' from the dataframe
df = df[['id', 'target']]
# Group the dataframe by 'id'
grouped = df.groupby('id')
# Count the number of targets for each id
counts = grouped['target'].count()
# Sort the dataframe by the count of targets in descending order
sorted_counts = counts.sort_values(ascending=False)
# Get the top 5 ids
top_5_ids = sorted_counts.head(5).index.tolist()
# Print the result
print(top_5_ids)