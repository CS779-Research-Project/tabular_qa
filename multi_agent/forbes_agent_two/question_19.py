import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'country'
countries = df['country']
# Count the occurrences of each country
country_counts = countries.value_counts()
# Get the bottom 2 countries
bottom_2_countries = country_counts.nsmallest(2)
# Print the result
print(list(bottom_2_countries.index))