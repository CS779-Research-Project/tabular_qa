import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the columns 'Total Fat (g)' and 'name' from the dataframe
df = df[['Total Fat (g)', 'name']]
# Sort the dataframe by 'Total Fat (g)' in descending order
df = df.sort_values('Total Fat (g)', ascending=False)
# Get the top 4 foods
top_4_foods = df['name'].head(4).tolist()
# Print the result
print(top_4_foods)