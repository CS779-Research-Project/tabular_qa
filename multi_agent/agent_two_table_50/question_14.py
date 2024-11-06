import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns 'author_name' and 'text' from the dataframe
df = df[['author_name', 'text']]
# Calculate the number of words in each post
df['word_count'] = df['text'].apply(lambda x: len(x.split()))
# Sort the dataframe based on the number of words in each post in ascending order
df = df.sort_values('word_count')
# Get the top 4 authors with the shortest posts
top_4_authors = df['author_name'].head(4)
# Extract the author names of these authors and convert them to a list
authors = top_4_authors.tolist()
# Print the result
print(authors)