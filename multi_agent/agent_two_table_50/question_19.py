import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the column 'text' from the dataframe
texts = df['text']
# Calculate the length of each text
text_lengths = texts.apply(lambda x: len(x.split()))
# Store the original texts and their word counts in a list of tuples
text_word_counts = list(zip(texts, text_lengths))
# Sort the texts by their length
sorted_texts = sorted(text_word_counts, key=lambda x: x[1])
# Get the 6 shortest texts
six_shortest_texts = sorted_texts[:6]
# Print the word counts of the 6 shortest texts
print([count for _, count in six_shortest_texts])