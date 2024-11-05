import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the column 'category' from the dataframe
categories = df['category']
# Group the dataframe by 'category' and count the number of occurrences in each category
category_counts = categories.value_counts()
# Sort the grouped dataframe by the count in ascending order
sorted_categories = category_counts.sort_values()
# Get the bottom 3 categories
bottom_3_categories = sorted_categories.index[:3]
# Print the result
print(list(bottom_3_categories))