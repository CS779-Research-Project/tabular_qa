import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the column 'Total Fat (g)' from the dataframe
total_fat = df['Total Fat (g)']
# Calculate the average total fat
average_total_fat = total_fat.mean()
# Print the result
print(f"The average total fat across all foods is: {average_total_fat:.2f} grams")