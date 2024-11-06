import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Check if 'user_followers_count' column exists in the dataframe
if 'user_followers_count' in df.columns:
    # Filter out the column 'user_followers_count' from the dataframe
    followers_count = df['user_followers_count']
    # Find the maximum value in the 'user_followers_count' column
    max_followers = followers_count.max()
    # Print the result
    print(max_followers)
else:
    print("Column 'user_followers_count' does not exist in the dataframe.")