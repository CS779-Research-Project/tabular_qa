import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the rows where'mention_ids' contains the specific user (e.g., "@exampleuser")
df_filtered = df[df['mention_ids'].apply(lambda x: "@exampleuser" in x)]
# Calculate the average number of retweets for these filtered tweets
average_retweets = df_filtered['retweets'].mean()
# Print the result
print(average_retweets)