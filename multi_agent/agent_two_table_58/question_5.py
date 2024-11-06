import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'Who are you most likely to vote for on election day?' from the dataframe
vote_choice = df['Who are you most likely to vote for on election day?']
# Filter the dataframe to get the respondents who are leaning towards voting for Joe Biden
joseph_biden_votes = vote_choice[vote_choice == 'Joe Biden']
# Count the number of these respondents
count_joseph_biden_votes = joseph_biden_votes.count()
# Print the result
print(count_joseph_biden_votes)