import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'How old are you?' from the dataframe
age_group = df['How old are you?']
# Define age groups
age_groups = {
    '18-24': '18-24',
    '25-34': '25-34',
    '35-44': '35-44',
    '45-54': '45-54',
    '55-64': '55-64',
    '65+': '65+'
}
# Replace age values with age groups
age_group = age_group.replace(age_groups)
# Count the frequency of each age group
age_count = age_group.value_counts()
# Find the most frequent age group
most_frequent_age_group = age_count.idxmax()
# Print the result
print(most_frequent_age_group)