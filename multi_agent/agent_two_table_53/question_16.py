import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'num_claims' from the dataframe
num_claims = df['num_claims']
# Sort the dataframe based on 'num_claims' in descending order
sorted_df = num_claims.sort_values(ascending=False)
# Get the top 4 rows
top_4 = sorted_df.head(4)
# Extract the 'num_claims' values from these rows
top_4_claims = top_4.tolist()
# Print the result
print(top_4_claims)