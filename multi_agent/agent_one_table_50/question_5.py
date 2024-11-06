import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the column 'text' from the dataframe
text = df['text']
# Split the 'text' column into individual words
words = text.str.split()
# Calculate the length of each post (number of words)
lengths = words.apply(len)
# Find the maximum length
max_length = lengths.max()
# Print the result
print(max_length)