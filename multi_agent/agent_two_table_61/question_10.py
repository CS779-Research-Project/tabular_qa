import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the columns 'Year_Month' and 'Rating' from the dataframe
df = df[['Year_Month', 'Rating']]
# Convert 'Year_Month' column to datetime if it's not already
if pd.api.types.is_categorical_dtype(df['Year_Month']):
    df['Year_Month'] = pd.to_datetime(df['Year_Month'])
# Filter the dataframe to get the reviews with a rating of 1 (most negative)
negative_reviews = df[df['Rating'] == 1]
# Find the earliest 'Year_Month' value among these negative reviews
first_negative_review_date = negative_reviews['Year_Month'].min()
# Print the result
print(first_negative_review_date)