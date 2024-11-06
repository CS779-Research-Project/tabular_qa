import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the column 'author_handler' from the dataframe
author_handler = df['author_handler']
# Group the dataframe by 'author_handler'
grouped = df.groupby('author_handler')
# Count the number of tweets for each author handler
counts = grouped.size()
# Sort the dataframe by the count in descending order
sorted_counts = counts.sort_values(ascending=False)
# Get the top 3 author handlers
top_3_handlers = sorted_counts.index[:3]
# Print the result
print(top_3_handlers.tolist())