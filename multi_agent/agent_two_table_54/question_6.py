import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Check if the'retweets' column exists in the dataframe
if'retweets' in df.columns:
    # Filter out the column'retweets' from the dataframe
    retweets = df['retweets']
    # Find the maximum value in the'retweets' column
    max_retweets = retweets.max()
    # Print the result
    print(max_retweets)
else:
    print("Column'retweets' does not exist in the dataframe.")