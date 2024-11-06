import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the column 'Calories (kcal)' from the dataframe
calories = df['Calories (kcal)']
# Sort the dataframe in descending order based on 'Calories (kcal)'
calories_sorted = calories.sort_values(ascending=False)
# Get the top 5 rows
top_5_calories = calories_sorted.head(5)
# Extract the 'Calories (kcal)' values into a list
calories_list = top_5_calories.tolist()
# Print the list
print(calories_list)