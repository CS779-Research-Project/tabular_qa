import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the column 'Country' from the dataframe
countries = df['Country']
# Count the number of transactions for each country
country_counts = countries.value_counts()
# Get the top 2 countries
top_countries = country_counts.head(2).index.tolist()
# Print the result
print(top_countries)