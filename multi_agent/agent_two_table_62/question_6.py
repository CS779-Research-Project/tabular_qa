import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Filter out the column 'links' from the dataframe
links = df['links']
# Calculate the average number of links per tweet
average_links = float(links.mean())
# Print the result
print(average_links)