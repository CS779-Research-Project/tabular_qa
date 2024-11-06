import pandas as pd

# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')

# Filter out the 'photos' column from the DataFrame
photos = df['photos']

# Calculate the average number of photos
average_photos = photos.mean()

# Print the result
print(average_photos)