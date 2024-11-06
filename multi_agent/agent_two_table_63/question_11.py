import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the columns 'name' and 'y' from the DataFrame
df = df[['name', 'y']]
# Find the maximum value in the 'y' column
highest_y = df['y'].max()
# Filter the DataFrame to get the entity(s) with the highest y-coordinate
entities_with_highest_y = df[df['y'] == highest_y]['name']
# Print the name(s) of the entity(s) with the highest y-coordinate
print(entities_with_highest_y.iloc[0])