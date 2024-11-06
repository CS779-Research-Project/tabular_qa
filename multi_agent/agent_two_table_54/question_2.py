import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the columns 'author_id<gx:category>','mention_names<gx:list[category]>', and'retweets<gx:number>' from the dataframe
df = df[['author_id<gx:category>','mention_names<gx:list[category]>','retweets<gx:number>']]
# Find the most mentioned user
most_mentioned_user = df['mention_names<gx:list[category]>'].value_counts().index[0]
# Find the most retweeted mentioned user
most_retweeted_user = df[df['retweets<gx:number>'] == df['retweets<gx:number>'].max()]['mention_names<gx:list[category]>'].values[0]
# Check if the most mentioned user is the same as the most retweeted mentioned user
is_same = most_mentioned_user == most_retweeted_user
# Print the result
print(is_same)