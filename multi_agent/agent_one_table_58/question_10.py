import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Select the column 'What is the highest degree or level of school you have *completed*?'
education = df['What is the highest degree or level of school you have *completed*?']
# Count the frequency of each category
education_counts = education.value_counts()
# Find the category with the highest frequency
most_common_education = education_counts.idxmax()
# Print the result
print(most_common_education)