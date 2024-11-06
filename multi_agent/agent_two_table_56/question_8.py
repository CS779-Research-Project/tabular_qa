import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Find the food with the highest calorie content
highest_calorie_food = df['Calories (kcal)'].idxmax()
# Print the name of the food
print(df.loc[highest_calorie_food, 'name'])