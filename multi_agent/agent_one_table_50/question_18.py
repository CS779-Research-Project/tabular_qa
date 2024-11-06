import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns'retweets' and 'favorites' from the dataframe
df = df[['retweets', 'favorites']]
# Sort the dataframe by 'favorites' in ascending order
df = df.sort_values(by='favorites')
# Select the top 4 rows
top_4_rows = df.head(4)
# Extract the'retweets' column from the selected rows
retweets = top_4_rows['retweets']
# Convert the extracted values to a list
retweets_list = retweets.tolist()
# Print the result
print(retweets_list)