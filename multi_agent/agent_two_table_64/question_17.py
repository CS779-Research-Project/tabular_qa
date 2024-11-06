import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Get the bottom 4 class types with the least combined total legs
bottom_4_classes = df.groupby('class_type')['legs'].sum().sort_values().head(4).index.tolist()
# Print the result
print(bottom_4_classes)