import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Get the top 4 class types by frequency
top_4_class_types = df['class_type'].value_counts().nlargest(4).index.tolist()
# Print the result
print(top_4_class_types)