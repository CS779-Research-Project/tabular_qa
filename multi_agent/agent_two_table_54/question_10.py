import pandas as pd
from collections import Counter
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the columns 'author_name<gx:category>' and'mention_names<gx:list[category]>' from the dataframe
df = df[['author_name<gx:category>','mention_names<gx:list[category]>']]
# Flatten the'mention_names<gx:list[category]>' column and count the frequency of each name
name_counts = Counter([name for sublist in df['mention_names<gx:list[category]>'].tolist() for name in sublist])
# Find the name with the highest frequency
most_common_name = name_counts.most_common(1)[0][0]
# Print the result
print(most_common_name)