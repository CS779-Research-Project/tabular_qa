import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter the dataframe with the column 'vote_intention'
vote_intention = df['vote_intention']
# Count the number of respondents who are likely to vote
likely_voters = vote_intention.value_counts()['likely']
# Print the result
print(f"Number of likely voters: {likely_voters}")