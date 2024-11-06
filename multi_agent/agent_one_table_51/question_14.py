import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the column 'type1' from the dataframe
type1 = df['type1']
# Count the frequency of each category in 'type1'
type1_counts = type1.value_counts()
# Sort the categories by frequency in descending order
top_4_categories = type1_counts.head(4).index.tolist()
# Print the result
print(top_4_categories)