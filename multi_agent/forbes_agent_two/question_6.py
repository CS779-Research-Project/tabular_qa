import pandas as pd

# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')

# Filter the dataframe to include only rows where the category is 'Technology'
technology_billionaires = df[df['category'] == 'Technology']

# Count the number of rows where the category is 'Technology'
count = technology_billionaires.shape[0]

# Print the result
print(f"Number of billionaires in the 'Technology' category: {count}")