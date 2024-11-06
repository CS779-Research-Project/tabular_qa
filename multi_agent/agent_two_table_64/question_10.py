import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the columns 'class_type' and 'legs' from the dataframe
df = df[['class_type', 'legs']]
# Group the dataframe by 'class_type'
grouped = df.groupby('class_type')
# Find the class type with the maximum number of legs
max_legs_class_type = grouped['legs'].sum().idxmax()
# Print the result
print(f"The class type with the most legs is: {max_legs_class_type}")