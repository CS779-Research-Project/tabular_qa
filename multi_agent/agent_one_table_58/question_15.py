import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'How old are you?' from the dataframe
age_column = df['How old are you?']
# Group the data by age
age_groups = age_column.groupby(age_column).size()
# Count the number of respondents in each age group
age_counts = age_groups.sort_values(ascending=False)
# Get the top 6 age groups
top_6_age_groups = age_counts.head(6)
# Print the result
print(top_6_age_groups)