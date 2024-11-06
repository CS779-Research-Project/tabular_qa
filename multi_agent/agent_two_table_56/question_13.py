import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the columns 'Total Sugar (g)' and 'name' from the dataframe
df = df[['Total Sugar (g)', 'name']]
# Sort the dataframe by 'Total Sugar (g)' in ascending order
df_sorted = df.sort_values(by='Total Sugar (g)')
# Get the top 3 foods with the least amount of sugar
top_3_foods = df_sorted['name'].head(3).tolist()
# Print the result
print(top_3_foods)