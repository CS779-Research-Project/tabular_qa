import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Profession' and 'Conscientiousness' from the dataframe
df = df[['Profession', 'Conscientiousness']]
# Group the dataframe by 'Profession' and calculate the mean 'Conscientiousness' for each profession
profession_conscientiousness = df.groupby('Profession')['Conscientiousness'].mean()
# Find the profession with the highest mean 'Conscientiousness'
highest_conscientiousness = profession_conscientiousness.idxmax()
# Print the result
print(highest_conscientiousness)