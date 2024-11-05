import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns'selfMade' and 'rank' from the dataframe
df = df[['selfMade', 'rank']]
# Filter the dataframe to get the non-self-made billionaires
non_self_made = df[df['selfMade'] == False]
# Sort the dataframe by 'finalWorth' in descending order
non_self_made_sorted = non_self_made.sort_values(by='finalWorth', ascending=False)
# Get the rank of the wealthiest non-self-made billionaire
wealthiest_rank = non_self_made_sorted.iloc[0]['rank']
# Print the result
print(wealthiest_rank)