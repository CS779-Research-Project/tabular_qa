import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the columns 'Calories (kcal)' and 'name' from the dataframe
df = df[['Calories (kcal)', 'name']]
# Sort the dataframe by 'Calories (kcal)' in descending order
df = df.sort_values('Calories (kcal)', ascending=False)
# Get the top 5 rows
top_5 = df.head(5)
# Extract the 'name' column from these rows
top_5_foods = top_5['name'].tolist()
# Print the result
for food in top_5_foods:
    print(food)