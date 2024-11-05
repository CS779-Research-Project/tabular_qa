import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Group the dataframe by 'category' and count the number of occurrences in each category
# Sort the grouped dataframe by the count in ascending order and get the bottom 3 categories
bottom_3_categories = df['category'].value_counts().nsmallest(3).index.tolist()
# Print the result
print(bottom_3_categories)