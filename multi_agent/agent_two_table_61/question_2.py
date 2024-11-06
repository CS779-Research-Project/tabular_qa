import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the column 'Rating' from the dataframe
ratings = df['Rating']
# Check if there are any ratings of 1
reviews_with_rating_1 = ratings == 1
# Print the result
print(reviews_with_rating_1.any())