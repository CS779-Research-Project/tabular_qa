import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'category'
df = df[df['category'] == 'Automotive']
# Sort the dataframe by 'finalWorth' in descending order
df = df.sort_values(by='finalWorth', ascending=False)
# Select the top 2 rows
top_2_final_worth = df['finalWorth'].head(2)
# Print the result
print(top_2_final_worth.tolist())