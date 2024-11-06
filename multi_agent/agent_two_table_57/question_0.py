import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'edu' from the dataframe
no_primary_edu = df[df['edu'].isin(['No education', 'Primary education'])]
# Check if there are any respondents who didn't complete primary education
no_primary_edu_count = no_primary_edu.shape[0]
# Print the result
print(no_primary_edu_count > 0)