import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Group the dataframe by'mention_names'
grouped = df.groupby('mention_names')
# Count the occurrences of each'mention_names'
counts = grouped.count()
# Sort the counts in descending order
sorted_counts = counts.sort_values(ascending=False)
# Get the top 4'mention_names' excluding the author
top_mentions = sorted_counts.index[1:5]
# Print the result
print(top_mentions.tolist())