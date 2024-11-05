import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column'source'
wealth_sources = df['source']
# Select the top 5 sources of wealth
top_5_sources = wealth_sources.value_counts().index[:5].tolist()
# Print the result
print(top_5_sources)