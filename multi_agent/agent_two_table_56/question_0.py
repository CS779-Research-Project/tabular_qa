import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the column 'Calories (kcal)' from the dataframe
calories = df['Calories (kcal)']
# Check if there are any foods with zero calories
zero_calories = calories.eq(0)
# Print the result
print("Are there any foods with zero calories?", zero_calories.any())