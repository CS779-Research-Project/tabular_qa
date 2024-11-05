import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the 'age' and 'country' columns from the dataframe
df = df[['age', 'country']]
# Sort the dataframe by 'age' in ascending order
df = df.sort_values(by='age')
# Get the country of the oldest billionaire
oldest_billionaire_country = df.iloc[0]['country']
# Print the result
print(oldest_billionaire_country)