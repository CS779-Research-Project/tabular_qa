import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the column 'legs' from the dataframe
legs = df['legs']
# Count the frequency of each unique value in the 'legs' column
legs_count = legs.value_counts()
# Sort the unique values by their frequency in descending order
legs_count_sorted = legs_count.sort_values(ascending=False)
# Select the top 4 most common values
top_4_legs = legs_count_sorted[:4].index.tolist()
# Print the result
print(top_4_legs)