import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the column 'text' from the dataframe
text = df['text']
# Calculate the length of each post (number of words)
lengths = text.str.split().str.len()
# Find the maximum length
max_length = lengths.max()
# Print the result
print(max_length)