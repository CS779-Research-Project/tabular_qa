import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the rows where 'category' is 'Technology'
tech_df = df[df['category'] == 'Technology']
# Sort the filtered dataframe by 'finalWorth' in descending order
tech_df = tech_df.sort_values('finalWorth', ascending=False)
# Select the top 6 rows
top_6_tech_df = tech_df.head(6)
# Extract the 'finalWorth' column from the selected rows
final_worths = top_6_tech_df['finalWorth'].tolist()
# Print the list
print(final_worths)