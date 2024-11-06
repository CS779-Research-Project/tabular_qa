import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the column 'Purpose of Loan' from the dataframe
purpose_of_loan = df['Purpose of Loan']
# Count the frequency of each category in the 'Purpose of Loan' column
purpose_of_loan_counts = purpose_of_loan.value_counts()
# Find the category with the highest frequency
most_common_purpose = purpose_of_loan_counts.idxmax()
# Print the result
print(f"The most common purpose of loans is '{most_common_purpose}' with a frequency of {purpose_of_loan_counts[most_common_purpose]}")