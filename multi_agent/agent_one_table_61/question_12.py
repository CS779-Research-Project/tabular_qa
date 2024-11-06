import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the 'Reviewer_Location' column from the dataframe
reviewer_locations = df['Reviewer_Location']
# Count the number of reviews for each location
location_counts = reviewer_locations.value_counts()
# Sort the locations by the number of reviews in descending order
sorted_locations = location_counts.sort_values(ascending=False)
# Select the top 3 locations with the most reviews
top_locations = sorted_locations.head(3).index.tolist()
# Print the result
print(top_locations)