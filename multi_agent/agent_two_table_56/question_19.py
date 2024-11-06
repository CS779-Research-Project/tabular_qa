import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the column 'Protein (g)' from the dataframe
protein = df['Protein (g)']
# Sort the dataframe by 'Protein (g)' in ascending order
protein_sorted = protein.sort_values()
# Get the top 6 lowest amounts of protein
top_6_lowest_protein = protein_sorted[:6]
# Convert the list to a string with a descriptive message
top_6_lowest_protein_str = ', '.join(map(str, top_6_lowest_protein.tolist()))
# Print the result
print(f"The top 6 lowest amounts of protein are: {top_6_lowest_protein_str}")