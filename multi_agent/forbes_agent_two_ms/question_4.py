import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'age' and 'philanthropyScore' from the dataframe
df = df[['age', 'philanthropyScore']]
# Find the oldest person in the dataframe
oldest_person = df['age'].max()
# Check if the philanthropy score of the oldest person is 5
result = df[(df['age'] == oldest_person) & (df['philanthropyScore'] == 5)].empty
# Print the result
print(result)