import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter the dataframe with the 'user_favourites_count' column
df_sorted = df.sort_values(by='user_favourites_count', ascending=False)
# Get the top 4 rows
top_4 = df_sorted.head(4)
# Extract the 'user_favourites_count' values from these rows
top_4_values = top_4['user_favourites_count'].tolist()
# Print the result
print(top_4_values)