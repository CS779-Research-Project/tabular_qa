import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the rows where Reviewer_Location is 'Australia'
df_australia = df[df['Reviewer_Location'] == 'Australia']
# Group the dataframe by Rating and get the count
rating_counts = df_australia.groupby('Rating').size()
# Get the top 3 ratings based on the count
top_3_ratings = rating_counts.nlargest(3).index.tolist()
# Print the result
print(top_3_ratings)