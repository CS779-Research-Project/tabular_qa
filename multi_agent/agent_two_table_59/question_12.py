import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column 'province' from the dataframe
province = df['province']
# Count the number of listings in each province
counts = province.value_counts()
# Sort the provinces by the number of listings in descending order
sorted_counts = counts.sort_values(ascending=False)
# If there is a tie, sort the tied provinces in reverse alphabetical order
sorted_counts = sorted_counts.sort_values(key=lambda x: x.index, ascending=False)
# Get the top 3 provinces
top_3_provinces = sorted_counts[:3].index.tolist()
# Print the result
print(top_3_provinces)