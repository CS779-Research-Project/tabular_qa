import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Profession' and 'Self-enhancement' from the dataframe and sort by 'Self-enhancement' in ascending order
df_sorted = df[['Profession', 'Self-enhancement']].sort_values(by='Self-enhancement')
# Get the bottom 2 professions
bottom_2_professions = df_sorted['Profession'].head(2).tolist()
# Print the result
print(bottom_2_professions)