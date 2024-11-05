import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column'selfMade'
df = df[df['selfMade'] == False]
# Filter the dataframe with the column 'rank'
df = df[df['rank']!= 0]
# Sort the dataframe by 'rank' in descending order
df = df.sort_values(by='rank', ascending=False)
# Select the top 5 rows
top_5_ranks = df['rank'].head(5).tolist()
# Print the result
print(top_5_ranks)