import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the columns 'Loan Duration - Months' and 'Number of Existing Loans' from the dataframe
df = df[['Loan Duration - Months', 'Number of Existing Loans']]
# Find the borrower with the longest loan duration
longest_loan_duration = df['Loan Duration - Months'].max()
# Find the borrower with the maximum number of existing loans
max_existing_loans = df['Number of Existing Loans'].max()
# Check if the borrower with the longest loan duration also has the maximum number of existing loans
result = (df['Loan Duration - Months'] == longest_loan_duration) & (df['Number of Existing Loans'] == max_existing_loans)
# Print the result
print(result.any())