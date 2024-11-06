import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the column'retweets' from the dataframe
retweets = df['retweets']
# Filter the dataframe to get rows where'retweets' is greater than 10000
more_than_10000_retweets = retweets > 10000
# Print the result
print(more_than_10000_retweets.any())