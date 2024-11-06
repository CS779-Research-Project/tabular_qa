import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'Which of the following best describes your ethnic heritage?' from the dataframe
ethnicity = df['Which of the following best describes your ethnic heritage?']
# Count the occurrences of each unique ethnic group
ethnicity_counts = ethnicity.value_counts()
# Get the top 3 unique ethnic groups based on their counts
top_3_ethnicities = ethnicity_counts.index[:3].tolist()
# Print the result
print(top_3_ethnicities)