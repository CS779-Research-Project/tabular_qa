import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'category'
category = df['category']
# Count the number of billionaires in each category
category_counts = category.value_counts()
# Select the bottom 3 categories
bottom_3_categories = category_counts[:3].index.tolist()
# Print the result
print(bottom_3_categories)