import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'How old are you?' from the dataframe
age_group = df['How old are you?']
# Count the frequency of each age group
age_count = age_group.value_counts()
# Find the most frequent age group
most_frequent_age_group = age_count.idxmax()
# Print the result
print(most_frequent_age_group)