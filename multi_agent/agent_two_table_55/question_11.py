import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the column 'Savings Account' from the dataframe
savings_account = df['Savings Account']
# Count the occurrences of each unique value in the 'Savings Account' column
counts = savings_account.value_counts()
# Find the most common value
most_common_status = counts.idxmax()
# Print the result
print(f"The most common savings account status is '{most_common_status}' with a count of {counts[most_common_status]}")