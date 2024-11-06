import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the columns 'Number of Existing Loans' and 'Loan Amount' from the dataframe
df = df[['Number of Existing Loans', 'Loan Amount']]
# Find the borrower with the maximum number of existing loans
max_loans = df['Number of Existing Loans'].max()
borrower_with_max_loans = df[df['Number of Existing Loans'] == max_loans]
# Find the maximum loan amount
max_loan_amount = df['Loan Amount'].max()
# Check if the borrower with the maximum number of existing loans also has the maximum loan amount
has_max_loan = borrower_with_max_loans['Loan Amount'].max() == max_loan_amount
# Print the result
print(has_max_loan)