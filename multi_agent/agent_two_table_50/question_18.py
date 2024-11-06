import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns'retweets' and 'favorites' from the dataframe
df = df[['retweets', 'favorites']]
# Sort the dataframe by 'favorites' in descending order and select the top 4 rows
top_4_rows = df.sort_values(by='favorites', ascending=False).head(4)
# Extract the'retweets' column from the selected rows
retweets_list = top_4_rows['retweets'].tolist()
# Print the result
print(retweets_list)