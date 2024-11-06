import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the column 'Number of Existing Loans' from the dataframe
existing_loans = df['Number of Existing Loans']
# Sort the filtered dataframe in descending order based on 'Number of Existing Loans'
sorted_loans = existing_loans.sort_values(ascending=False)
# Get the top 5 values
top_5_loans = sorted_loans.head(5).tolist()
# Print the result
print(top_5_loans)