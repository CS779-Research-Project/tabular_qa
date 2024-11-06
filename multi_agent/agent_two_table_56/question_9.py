import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the columns 'Total Sugar (g)' and 'name' from the dataframe
df = df[['Total Sugar (g)', 'name']]
# Find the food with the highest amount of sugar
food_with_most_sugar = df['Total Sugar (g)'].idxmax()
# Print the name of the food
print(df.loc[food_with_most_sugar, 'name'])