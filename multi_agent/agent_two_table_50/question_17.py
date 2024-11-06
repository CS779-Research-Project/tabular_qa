import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the column 'text' from the dataframe
texts = df['text']
# Calculate the length of each text
text_lengths = texts.apply(lambda x: len(x.split()))
# Get the top 3 longest texts
top_3_texts = texts[text_lengths.sort_values(ascending=False).head(3).index]
# Calculate the word count of each of these texts
word_counts = top_3_texts.apply(lambda x: len(x.split()))
# Store the word counts in a list
word_counts_list = word_counts.tolist()
# Print the list
print(word_counts_list)