import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'gender'
female_billionaires = df[df['gender'] == 'female']
# Filter the dataframe with the column 'rank'
top_4_ranks = female_billionaires.sort_values(by='rank', ascending=False).head(4)
# Get the ranks as a list
ranks = top_4_ranks['rank'].tolist()
# Print the result
print(ranks)