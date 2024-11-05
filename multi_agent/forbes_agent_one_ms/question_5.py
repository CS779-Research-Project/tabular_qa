import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the column 'age' from the dataframe
age = df['age']
# Find the age of the youngest billionaire
youngest_billionaire_age = age.min()
# Print the result
print(youngest_billionaire_age)