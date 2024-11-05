import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'age' and 'gender' from the dataframe
df = df[['age', 'gender']]
# Find the youngest billionaire
youngest_billionaire = df['age'].min()
youngest_billionaire_row = df[df['age'] == youngest_billionaire]
# Check if the youngest billionaire identifies as male
is_male = youngest_billionaire_row['gender'].values[0] =='male'
# Print the result
print(is_male)