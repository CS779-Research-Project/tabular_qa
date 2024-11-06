import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the columns 'Branch' and 'Rating' from the dataframe
df = df[['Branch', 'Rating']]
# Filter the dataframe to get the Disneyland_HongKong branch
disneyland_hongkong = df[df['Branch'] == 'Disneyland_HongKong']
# Calculate the average rating
average_rating = disneyland_hongkong['Rating'].mean()
# Print the result
print(average_rating)