import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'philanthropyScore' and 'age' from the dataframe
df = df[['philanthropyScore', 'age']]
# Filter the dataframe to get the rows where 'philanthropyScore' is 5
billionaires = df[df['philanthropyScore'] == 5]
# Sort the filtered dataframe by 'age' in ascending order
billionaires_sorted = billionaires.sort_values(by='age')
# Get the bottom 3 ages
bottom_3_ages = billionaires_sorted['age'].head(3).tolist()
# Print the result
print(bottom_3_ages)