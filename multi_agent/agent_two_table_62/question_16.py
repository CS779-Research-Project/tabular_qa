import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the columns 'id' and'retweets' from the dataframe
df = df[['id','retweets']]
# Sort the dataframe in descending order based on'retweets'
df = df.sort_values('retweets', ascending=False)
# Get the top 5 rows
top_5 = df.head(5)
# Extract the 'id' column from these rows
top_5_ids = top_5['id'].tolist()
# Print the result
print(top_5_ids)