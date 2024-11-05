import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the 'country' column from the dataframe
countries = df['country'].drop_duplicates()
# Count the number of billionaires in each country
country_counts = countries.value_counts()
# Sort the countries by the number of billionaires in ascending order
sorted_countries = country_counts.sort_values().index[:2]
# Convert the sorted countries into a list
bottom_countries = sorted_countries.tolist()
# Print the result
print(bottom_countries)