import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'philanthropyScore'
df = df[df['philanthropyScore'] == df['philanthropyScore'].max()]
# Get the gender of the billionaire with the highest philanthropy score
gender = df['gender'].iloc[0]
# Print the result
print(gender)