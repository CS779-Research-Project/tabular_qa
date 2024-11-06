import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the columns 'name' and 'y' from the dataframe
df = df[['name', 'y']]
# Get the bottom 3 entities
bottom_3_entities = df.nsmallest(3, 'y')['name'].tolist()
# Print the result
print(bottom_3_entities)