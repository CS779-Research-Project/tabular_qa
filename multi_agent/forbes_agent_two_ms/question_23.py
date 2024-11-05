import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'gender' and 'rank' from the dataframe
df = df[['gender', 'rank']]
# Filter the dataframe to get the rows where 'gender' is 'female'
female_df = df[df['gender'] == 'female']
# Sort the filtered dataframe by 'rank' in ascending order
female_df = female_df.sort_values('rank')
# Get the top 4 ranks
top_4_ranks = female_df['rank'].head(4)
# Print the result
print(top_4_ranks.tolist())