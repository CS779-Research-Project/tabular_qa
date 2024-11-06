import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns 'author_name' and 'type' from the dataframe
df = df[['author_name', 'type']]
# Group the dataframe by 'author_name'
grouped = df.groupby('author_name')
# For each group, count the number of rows where 'type' is 'original'
original_counts = grouped['type'].apply(lambda x: (x == 'original').sum())
# Find the author with the maximum count of 'original'
max_original_count = original_counts.max()
max_original_author = original_counts.idxmax()
# Check if this author's 'author_name' has the longest length
longest_name = df['author_name'].apply(len).idxmax()
if max_original_author == longest_name:
    # If yes, return True, else return False
    print(True)
else:
    print(False)