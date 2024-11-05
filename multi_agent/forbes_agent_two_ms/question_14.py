import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'rank' and 'title' from the dataframe
df = df[['rank', 'title']]
# Find the row with the lowest rank
lowest_rank = df['rank'].min()
person = df[df['rank'] == lowest_rank]
# Get the title of the person
title = person['title'].iloc[0]
# Print the result
print(title)