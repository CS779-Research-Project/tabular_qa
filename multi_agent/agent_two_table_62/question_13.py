import pandas as pd
import numpy as np
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the column 'lang' from the dataframe
lang = df['lang']
# Get the unique values of 'lang'
unique_langs = lang.unique()
# Sort the unique values in ascending order
sorted_indices = np.argsort(unique_langs)
sorted_langs = unique_langs[sorted_indices]
# Get the first two values from the sorted list
bottom_two_languages = sorted_langs[:2]
# Print the result
print(bottom_two_languages)