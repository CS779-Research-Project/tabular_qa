import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the column 'links' from the dataframe
links = df['links']
# Check if there are any empty lists in the 'links' column
empty_links = links.apply(lambda x: len(x) == 0)
# Convert the result to a boolean value
result = empty_links.any()
# Print the result
print(result)