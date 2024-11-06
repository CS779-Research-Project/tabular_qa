import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the column 'class_type' from the dataframe
class_type = df['class_type']
# Count the occurrences of each class type
class_counts = class_type.value_counts()
# Find the class type with the highest count
most_common_class_type = class_counts.idxmax()
# Print the result as a category
print(pd.api.types.CategoricalDtype(categories=class_counts.index, ordered=True).type_of(most_common_class_type))