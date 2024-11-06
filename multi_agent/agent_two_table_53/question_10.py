import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'lang' from the dataframe
lang = df['lang']
# Print the unique values in the 'lang' column
unique_languages = lang.unique().tolist()
# Print the result
print(unique_languages)