import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns 'author_name' and 'text' from the dataframe
df = df[['author_name', 'text']]
# Calculate the length of each text
df['text_length'] = df['text'].apply(len)
# Group the dataframe by 'author_name' and get the post with the maximum length
max_length_post = df.loc[df.groupby('author_name')['text_length'].idxmax()]
# Get the 'author_name' of the post
author_name = max_length_post['author_name'].values[0]
# Print the result
print(author_name)