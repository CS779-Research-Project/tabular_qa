import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the columns 'Branch' and 'Rating' from the dataframe
df = df[['Branch', 'Rating']]
# Filter the dataframe to get the ratings for Disneyland_HongKong
disneyland_hongkong_ratings = df[df['Branch'] == 'Disneyland_HongKong']
# Find the two smallest ratings
bottom_2_ratings = disneyland_hongkong_ratings['Rating'].nsmallest(2).tolist()
# Print the result
print(bottom_2_ratings)