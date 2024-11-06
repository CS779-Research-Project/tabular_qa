import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'title' from the dataframe
titles = df['title']
# Check if the word 'communication' is present in each title
has_communication = titles.apply(lambda title: 'communication' in title.lower()).any()
# Print the result
print(has_communication)