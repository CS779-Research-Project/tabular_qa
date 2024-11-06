import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the columns 'id' and 'weight' from the dataframe
df = df[['id', 'weight']]
# Sort the dataframe in descending order based on 'weight'
df = df.sort_values(by='weight', ascending=False)
# Get the top 5 'id' values
top_5_ids = df['id'].head(5).tolist()
# Print the result
print(top_5_ids)