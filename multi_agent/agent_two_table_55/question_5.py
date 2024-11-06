import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter the dataframe to get the borrowers with more than 1 existing loan
more_than_one_loan = df[df['Number of Existing Loans'] > 1]
# Count the number of such borrowers
count = len(more_than_one_loan)
# Print the result
print(count)