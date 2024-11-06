import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column 'color' from the dataframe
color = df['color']
# Count the frequency of each color
color_counts = color.value_counts()
# Get the top 3 most common colors
top_3_colors = color_counts[:3].index.tolist()
# Print the result
print(top_3_colors)