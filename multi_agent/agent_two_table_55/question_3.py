import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the columns 'Age' and 'Loan Amount' from the dataframe
df = df[['Age', 'Loan Amount']]
# Find the maximum age
max_age = df['Age'].max()
# Find the maximum loan amount
max_loan_amount = df['Loan Amount'].max()
# Filter the dataframe for the oldest borrower
oldest_borrower = df[df['Age'] == max_age]
# Check if the loan amount for the oldest borrower is the highest
is_same = oldest_borrower['Loan Amount'].max() == max_loan_amount
# Print the result
print(is_same)