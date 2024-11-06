import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the columns 'Branch' and 'Rating' from the dataframe
branches = df[['Branch', 'Rating']]
# Group the dataframe by 'Branch' and calculate the average rating
average_ratings = branches.groupby('Branch')['Rating'].mean()
# Get the branches with the lowest 2 average ratings
bottom_2_branches = average_ratings.nsmallest(2).index.tolist()
# Print the result
print(bottom_2_branches)