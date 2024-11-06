import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the column 'Protein (g)' from the dataframe
protein = df['Protein (g)']
# Find the maximum value in the 'Protein (g)' column
max_protein = protein.max()
# Print the result
print(f"The highest amount of protein found in a food item is: {max_protein} grams")