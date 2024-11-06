import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Get the top 3 most common colors
top_3_colors = df['color'].value_counts().nlargest(3).index.tolist()
# Print the result
print(top_3_colors)