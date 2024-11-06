import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the columns 'name' and 'x' from the dataframe and sort by 'x' in descending order
df = df[['name', 'x']].sort_values(by='x', ascending=False).head(4)
# Get the top 4 entities
top_4_entities = df['name'].tolist()
# Print the result
print(top_4_entities)