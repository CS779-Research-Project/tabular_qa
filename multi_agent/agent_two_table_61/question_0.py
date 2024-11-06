import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the columns 'Reviewer_Location' and 'Rating' from the dataframe
df = df[['Reviewer_Location', 'Rating']]
# Filter the dataframe to get the reviews from Australia
australian_reviews = df[df['Reviewer_Location'] == 'Australia']
# Check if all the ratings for these reviews are greater than 3
all_positive_reviews = australian_reviews['Rating'] > 3
# Print the result
print(all_positive_reviews.all())