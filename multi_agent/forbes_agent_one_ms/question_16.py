import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the column'source' from the dataframe
source = df['source']
# Get the unique sources of wealth
unique_sources = source.unique()
# Get the top 5 sources
top_sources = unique_sources[:5]
# Print the result
print(top_sources)