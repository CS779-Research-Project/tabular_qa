import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'User self- placement on Progressive-Conservative economic values axis' from the dataframe
progressive_conservative_values = df['User self- placement on Progressive-Conservative economic values axis']
# Count the occurrences of each value
counts = progressive_conservative_values.value_counts()
# Sort the counts in descending order
sorted_counts = counts.sort_values(ascending=False)
# Get the top 4 values
top_4 = sorted_counts[:4].index.tolist()
# Print the result
print(top_4)