import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the rows where 'legendary' is False
non_legendary_df = df[df['legendary'] == False]
# Sort the dataframe by 'total' in ascending order
sorted_df = non_legendary_df.sort_values('total')
# Select the first 6 rows
top_six_df = sorted_df.head(6)
# Extract the 'total' column from these rows
top_six_total = top_six_df['total'].tolist()
# Print the result
print(top_six_total)