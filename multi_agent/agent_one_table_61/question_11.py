import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the columns 'Reviewer_Location' and 'Rating' from the dataframe
df = df[['Reviewer_Location', 'Rating']]
# Group the dataframe by 'Reviewer_Location' and calculate the average rating for each location
grouped_df = df.groupby('Reviewer_Location')['Rating'].mean().reset_index()
# Sort the grouped dataframe by average rating in descending order and then by 'Reviewer_Location' in ascending order
sorted_df = grouped_df.sort_values(by=['Rating', 'Reviewer_Location'], ascending=[False, True])
# Get the first row of the sorted dataframe
top_location = sorted_df.iloc[0]
# Get the 'Reviewer_Location' from the first row
reviewer_location = top_location['Reviewer_Location']
# Print the result
print(reviewer_location)