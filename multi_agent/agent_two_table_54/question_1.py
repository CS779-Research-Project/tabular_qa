import pandas as pd
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the relevant columns 'author_id<gx:category>', 'user_favourites_count<gx:number>','retweets<gx:number>' from the dataframe
df = df[['author_id<gx:category>', 'user_favourites_count<gx:number>','retweets<gx:number>']]
# Group the dataframe by 'author_id<gx:category>'
grouped = df.groupby('author_id<gx:category>')
# For each group, check if the maximum 'user_favourites_count<gx:number>' is equal to the maximum'retweets<gx:number>'
all_equal = grouped['user_favourites_count<gx:number>'].max() == grouped['retweets<gx:number>'].max()
# If all groups satisfy the condition, print True, else print False
print(all_equal.all())