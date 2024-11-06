import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the column 'Loan Amount' from the dataframe
loan_amount = df['Loan Amount']
# Sort the dataframe by 'Loan Amount' in descending order
sorted_loan_amount = loan_amount.sort_values(ascending=False)
# Get the top 3 loan amounts
top_3_loan_amounts = sorted_loan_amount.head(3).tolist()
# Print the result
print(top_3_loan_amounts)