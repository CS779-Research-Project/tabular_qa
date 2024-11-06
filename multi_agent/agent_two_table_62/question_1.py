import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the column'retweets' from the dataframe
retweets = df['retweets']
# Check if there are any non-zero values in the'retweets' column
has_retweeted = retweets.any()
# Convert the result to a boolean value
has_retweeted = bool(has_retweeted)
# Print the result
print(has_retweeted)