import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'How old are you?' from the dataframe
age_column = df['How old are you?']
# Group the data by age
age_groups = age_column.groupby(age_column).size()
# Sort the age groups by the number of respondents in descending order
sorted_age_groups = age_groups.sort_values(ascending=False)
# Get the top 6 age groups
top_6_age_groups = sorted_age_groups.head(6)
# Print the result
print(top_6_age

Here is the output of the code-block present in the above conversation : 

