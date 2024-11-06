import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the columns 'lang' and'retweets' from the dataframe
df = df[['lang','retweets']]
# Group the dataframe by 'lang'
grouped = df.groupby('lang')
# Find the language with the maximum number of retweets
max_retweets_lang = grouped['retweets'].sum().idxmax()
max_retweets_count = grouped['retweets'].sum().max()
# Print the result
print(f"The language with the most retweets is {max_retweets_lang} with {max_retweets_count} retweets.")