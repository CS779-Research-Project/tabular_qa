import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the columns 'Reviewer_Location' and 'Rating' from the dataframe
df = df[['Reviewer_Location', 'Rating']]
# Group the dataframe by 'Reviewer_Location' and calculate the average rating
average_ratings = df.groupby('Reviewer_Location')['Rating'].mean()
# Sort the average ratings in ascending order
sorted_average_ratings = average_ratings.sort_values()
# Get the bottom 3 locations
bottom_3_locations = sorted_average_ratings.index[:3].tolist()
# Print the result
print(bottom_3_locations)