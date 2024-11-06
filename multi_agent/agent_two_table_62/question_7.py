import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])
# Filter the dataframe to get the tweets from 2018
tweets_2018 = df[df['date'].dt.year == 2018]
# Count the number of tweets
num_tweets = tweets_2018.shape[0]
# Print the result
print(num_tweets)