import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the columns 'Loan Amount' and 'Loan Duration - Months' from the dataframe
df = df[['Loan Amount', 'Loan Duration - Months']]
# Find the maximum loan amount
max_loan_amount = df['Loan Amount'].max()
# Find the maximum loan duration
max_loan_duration = df['Loan Duration - Months'].max()
# Check if the borrower with the maximum loan amount also has the maximum loan duration
is_same_borrower = df[(df['Loan Amount'] == max_loan_amount) & (df['Loan Duration - Months'] == max_loan_duration)].shape[0] == 1
# Print the result
print(is_same_borrower)