import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'Are you registered to vote?' from the dataframe
registered_to_vote = df['Are you registered to vote?']
# Count the number of 'Yes' values in the column
num_registered_to_vote = registered_to_vote.value_counts()['Yes']
# Print the result
print(num_registered_to_vote)