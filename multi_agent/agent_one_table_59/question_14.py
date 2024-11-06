import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column'make' from the dataframe
make = df['make']
# Get the unique values of'make'
unique_makes = make.unique()
# Get the top 5 most prevalent'make' values
top_5_makes = unique_makes[:5]
# Print the result
print(top_5_makes)