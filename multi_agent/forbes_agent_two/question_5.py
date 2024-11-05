import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Convert the 'age' column to integers
df['age'] = df['age'].astype(int)
# Filter the dataframe with the column 'age'
age = df['age']
# Find the minimum age
youngest_billionaire_age = age.min()
# Print the result
print(youngest_billionaire_age)