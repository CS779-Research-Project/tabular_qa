import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe to get the oldest billionaire
oldest_billionaire = df[df['age'] == df['age'].max()]
# Get the country of origin
country = oldest_billionaire['country'].iloc[0]
# Print the result
print(country)