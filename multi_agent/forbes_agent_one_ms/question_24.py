import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the rows where 'category' is 'Automotive'
df_automotive = df[df['category'] == 'Automotive']
# Sort the filtered dataframe by 'finalWorth' in descending order
df_automotive_sorted = df_automotive.sort_values('finalWorth', ascending=False)
# Select the top 2 rows
top_2_automotive = df_automotive_sorted.head(2)
# Extract the 'finalWorth' values from the selected rows
final_worth_values = top_2_automotive['finalWorth'].tolist()
# Print the result
print(final_worth_values)