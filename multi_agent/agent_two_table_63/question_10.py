import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the columns 'pic' and 'weight' from the dataframe
df = df[['pic', 'weight']]
# Find the row with the maximum weight value
max_weight_row = df[df['weight'] == df['weight'].max()]
# Extract the 'pic' value (URL) from the row with the maximum weight
picture_url = max_weight_row.iloc[0]['pic']
# Print the result
print(picture_url)