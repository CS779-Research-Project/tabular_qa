import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the columns 'Branch' and 'Rating' from the dataframe
branch_rating = df[['Branch', 'Rating']]
# Group the dataframe by 'Branch' and calculate the average rating for each branch
average_rating = branch_rating.groupby('Branch')['Rating'].mean()
# Find the branch with the lowest average rating
lowest_average_rating_branch = average_rating.idxmin()
# Print the result
print(lowest_average_rating_branch)