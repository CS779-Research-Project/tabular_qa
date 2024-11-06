import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the 'Profession' and 'n' columns from the dataframe
df = df[['Profession', 'n']]
# Group the dataframe by 'Profession' and get the count of each profession
profession_counts = df.groupby('Profession').size()
# Get the profession with the highest count
most_common_profession = profession_counts.idxmax()
# Print the result
print(most_common_profession)