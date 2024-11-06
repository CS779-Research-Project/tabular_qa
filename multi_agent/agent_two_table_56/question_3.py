import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the column 'Protein (g)' from the dataframe
protein = df['Protein (g)']
# Check if there are any foods with zero protein
foods_with_zero_protein = protein == 0
# Convert the result to boolean
result = foods_with_zero_protein.any()
# Print the result with a clear message
print(f"Are there foods that do not contain protein? {'Yes' if result else 'No'}")