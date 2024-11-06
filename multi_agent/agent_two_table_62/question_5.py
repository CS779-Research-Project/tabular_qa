import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the column'retweets' from the dataframe
retweets = df['retweets']
# Calculate the average number of retweets
average_retweets = retweets.mean()
# Print the result
print(f"The average number of retweets is: {average_retweets:.2f}")