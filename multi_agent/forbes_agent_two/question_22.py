import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'category'
technology_billionaires = df[df['category'] == 'Technology']
# Sort the dataframe by 'finalWorth' in descending order
technology_billionaires = technology_billionaires.sort_values(by='finalWorth', ascending=False)
# Select the top 6 rows
top_6_billionaires = technology_billionaires['finalWorth'].head(6).tolist()
# Print the result
print(top_6_billionaires)