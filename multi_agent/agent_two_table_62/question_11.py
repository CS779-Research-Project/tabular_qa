import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the rows where 'lang' is 'en'
df_en = df[df['lang'] == 'en']
# Calculate the average number of'retweets' for these rows
avg_retweets = df_en['retweets'].mean()
# Print the result
print(avg_retweets)