import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Profession' and 'Agreeableness' from the dataframe
df = df[['Profession', 'Agreeableness']]
# Sort the dataframe based on 'Agreeableness' in ascending order
df_sorted = df.sort_values(by='Agreeableness')
# Get the bottom 4 professions
bottom_4_professions = df_sorted['Profession'].head(4)
# Print the result
print(bottom_4_professions.tolist())