import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Count the frequency of each class type
class_type_counts = df['class_type'].value_counts()
# Get the class types with the least number of animals
least_common_class_types = class_type_counts.nsmallest(3).index.tolist()
# Print the result
print(least_common_class_types)