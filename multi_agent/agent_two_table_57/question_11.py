import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Select the 'lang' column
lang = df['lang']
# Count the frequency of each language
language_counts = lang.value_counts()
# Find the language with the highest frequency
most_common_language = language_counts.idxmax()
# Print the result
print(most_common_language)