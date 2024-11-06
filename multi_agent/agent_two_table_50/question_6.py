import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the column'retweets' from the dataframe
retweets = df['retweets']
# Calculate the sum of retweets
total_retweets = retweets.sum()
# Print the result
print(f"Total number of retweets: {total_retweets}")