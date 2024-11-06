import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the columns 'Review_ID' and 'Rating' from the dataframe
df = df[['Review_ID', 'Rating']]
# Sort the dataframe by 'Rating' in ascending order
df = df.sort_values(by='Rating')
# Get the bottom 4 'Review_ID'
bottom_4_reviews = df['Review_ID'].head(4)
# Handle ties by keeping the lowest IDs
bottom_4_reviews = bottom_4_reviews.drop_duplicates().reset_index(drop=True)
# Print the result
print(bottom_4_reviews.tolist())