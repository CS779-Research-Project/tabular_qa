import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'lang' from the dataframe
lang = df['lang']
# Count the frequency of each language
language_counts = lang.value_counts()
# Sort the languages by frequency
sorted_languages = language_counts.sort_values(ascending=False)
# Get the top 6 most common languages
top_6_languages = sorted_languages[:6].index.tolist()
# Print the result
print(top_6_languages)