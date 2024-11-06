import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Select the column 'class_type'
class_type = df['class_type']
# Count the number of unique class_type
unique_class_type = class_type.nunique()
# Print the result
print(unique_class_type)