import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column'make' from the dataframe
make = df['make']
# Count the frequency of each make
make_counts = make.value_counts()
# Find the most common make(s)
most_common_makes = make_counts[make_counts == make_counts.max()]
# Sort the most common makes alphabetically
most_common_makes = most_common_makes.sort_values().index.tolist()
# Print the result
print(most_common_makes)