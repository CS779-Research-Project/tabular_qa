import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the column 'Calories (kcal)' from the dataframe
calories = df['Calories (kcal)']
# Filter the dataframe to get the foods with more than 500 kcal
high_calorie_foods = calories[calories > 500]
# Count the number of such foods
count = len(high_calorie_foods)
# Print the result
print(count)