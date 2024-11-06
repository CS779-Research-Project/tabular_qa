import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Select the 'photos' column
photos = df['photos']
# Sort the DataFrame by 'photos' in descending order
sorted_photos = photos.sort_values(ascending=False)
# Get the top 5 entries
top_5_photos = sorted_photos.head(5)
# Print the result
print(top_5_photos)