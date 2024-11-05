import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns'selfMade' and 'rank' from the dataframe
df = df[['selfMade', 'rank']]
# Sort the dataframe by 'rank' in ascending order
df = df.sort_values(by='rank')
# Get the top 5 ranks
top_5_ranks = df['rank'].head(5).tolist()
# Print the result
print(top_5_ranks)