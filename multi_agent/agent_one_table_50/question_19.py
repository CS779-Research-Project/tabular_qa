import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the column 'text' from the dataframe
texts = df['text']
# Calculate the length of each text
text_lengths = texts.apply(lambda x: len(x.split()))
# Sort the texts by their length
sorted_texts = text_lengths.sort_values()
# Get the 6 shortest texts
six_shortest_texts = sorted_texts[:6]
# Print the word counts of the 6 shortest texts
print(six_shortest_texts.tolist())