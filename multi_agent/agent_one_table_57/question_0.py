import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'edu' from the dataframe
edu = df['edu']
# Check if there are any respondents who didn't complete primary education
no_primary_edu = edu.isin(['No education', 'Primary education'])
no_primary_edu = no_primary_edu[no_primary_edu == True].any()
# Print the result
print(no_primary_edu)