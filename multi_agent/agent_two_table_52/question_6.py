import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Profession', 'Extraversion', and 'n' from the dataframe
df = df[['Profession', 'Extraversion', 'n']]
# Group the dataframe by 'Profession'
grouped = df.groupby('Profession')
# For each group, calculate the average 'Extraversion'
average_extraversion = grouped['Extraversion'].mean()
# Find the profession with the highest 'n'
profession_with_highest_n = grouped['n'].idxmax()
# Get the average 'Extraversion' for that profession
average_extraversion_for_highest_n = average_extraversion[profession_with_highest_n]
# Print the result
print(average_extraversion_for_highest_n)