import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'city' and 'country' from the dataframe
df = df[['city', 'country']]
# Count the number of unique cities in the dataframe
unique_cities = df['city'].nunique()
# Count the number of unique cities in the United States
us_cities = df[df['country'] == 'United States']['city'].nunique()
# Compare the two counts
is_most_billionaires_in_us = us_cities == unique_cities
# Print the result
print(f"Are the most billionaires in the United States? {is_most_billionaires_in_us}")