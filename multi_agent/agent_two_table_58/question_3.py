import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter the dataframe with the column 'Who did you vote for in the 2016 Presidential election? (Four years ago)'
voted_2016 = df['Who did you vote for in the 2016 Presidential election? (Four years ago)']
# Filter the dataframe with the column 'Who are you most likely to vote for on election day?'
likely_voted_2020 = df['Who are you most likely to vote for on election day?']
# Check if there are respondents who have shifted their voting preference
shifted_voting_preference = (voted_2016!= likely_voted_2020).any()
# Print the result
print(shifted_voting_preference)