import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the column 'category' from the dataframe
category = df['category']
# Filter the dataframe to get the rows where 'category' is 'Technology'
technology_category = category[category == 'Technology']
# Count the number of rows using shape attribute
num_billionaires = technology_category.shape[0]
# Print the result
print(num_billionaires)