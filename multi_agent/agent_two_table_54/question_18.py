import pandas as pd
from collections import Counter
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Flatten the'mention_names' column
mention_names_flat = [item for sublist in df['mention_names'] for item in sublist]
# Count the frequency of each mention name
mention_counts = Counter(mention_names_flat)
# Sort the mention names by their frequency in descending order
sorted_mentions = mention_counts.most_common()
# Get the top 5 mention names
top_mentions = [mention[0] for mention in sorted_mentions[:5]]
# Print the result
print(top_mentions)