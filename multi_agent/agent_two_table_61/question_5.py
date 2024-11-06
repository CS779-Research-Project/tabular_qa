import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter the dataframe to get the Disneyland_HongKong branch
disneyland_hongkong = df[df['Branch'] == 'Disneyland_HongKong']
# Calculate the average rating
average_rating = disneyland_hongkong['Rating'].mean()
# Print the result
print(f"The average rating for Disneyland_HongKong is {average_rating:.2f}")