import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'Vote Intention' from the dataframe
vote_intention = df['Vote Intention']
# Check if any value in the 'Vote Intention' column is 'No'
no_vote = 'No' in vote_intention.values
# Print the result
print(no_vote.any())