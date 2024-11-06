import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the columns 'class_type' and 'legs' from the dataframe
df = df[['class_type', 'legs']]
# Group the dataframe by 'class_type' and sum the 'legs'
grouped_df = df.groupby('class_type')['legs'].sum().reset_index()
# Sort the grouped dataframe by the sum of 'legs' in descending order
sorted_df = grouped_df.sort_values('legs', ascending=False)
# Get the top 5 class types with the most combined total legs
top_5_classes = sorted_df['class_type'].head(5).tolist()
# Print the result
print(top_5_classes)