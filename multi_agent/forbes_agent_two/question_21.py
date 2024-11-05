import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'philanthropyScore'
df = df[df['philanthropyScore'] == 5]
# Filter the dataframe with the column 'age'
df = df[df['age']!= 0]
# Sort the dataframe by 'age' in ascending order and select the bottom 3 ages
bottom_3_ages = df.sort_values(by='age', ascending=True)['age'].head(3).tolist()
# Print the result
print(bottom_3_ages)