import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the columns 'text' and 'favorites' from the dataframe
df = df[['text', 'favorites']]
# Find the tweet with the maximum number of favorites
max_favorites = df['favorites'].max()
tweet = df[df['favorites'] == max_favorites]['text']
# Print the text of the tweet as a string
print(str(tweet.iloc[0]))