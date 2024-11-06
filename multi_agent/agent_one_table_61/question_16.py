import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the columns 'Review_ID' and 'Rating' from the dataframe
df = df[['Review_ID', 'Rating']]
# Sort the dataframe in descending order based on 'Rating'
df = df.sort_values(by='Rating', ascending=False)
# Get the top 5 'Review_ID'
top_5_review_ids = df['Review_ID'].head(5).tolist()
# Handle ties by keeping the highest IDs
top_5_review_ids = df.drop_duplicates(subset='Review_ID', keep='first').head(5)['Review_ID'].tolist()
# Print the result
print(top_5_review_ids)