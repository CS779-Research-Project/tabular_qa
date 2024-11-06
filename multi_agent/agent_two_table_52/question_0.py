import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Calculate the maximum level of Extraversion
max_extraversion = df['Extraversion'].max()
# Calculate the maximum level of Agreeableness
max_agreeableness = df['Agreeableness'].max()
# Compare the maximum levels and print the result
print(max_extraversion > max_agreeableness)