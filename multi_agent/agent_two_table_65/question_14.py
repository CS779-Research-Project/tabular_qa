import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Count the number of transactions for each country
country_counts = df['Country'].value_counts()
# Get the top 2 countries
top_countries = country_counts.head(2).index.tolist()
# Print the result
print(top_countries)