import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'Are you registered to vote?' from the dataframe
registered_to_vote = df['Are you registered to vote?']
# Check if there are any 'False' values in the filtered column
unregistered_to_vote = registered_to_vote.value_counts()['False']
# Print the result
print(unregistered_to_vote)