import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Count the number of 'Yes' values in the column 'Are you registered to vote?'
num_registered_to_vote = df['Are you registered to vote?'].value_counts()['Yes']
# Print the result
print(num_registered_to_vote)