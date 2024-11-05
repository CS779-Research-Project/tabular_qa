import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the columns 'city' and 'country'
city_country = df[['city', 'country']]
# Count the number of billionaires in each city
city_count = city_country.groupby('city', observed=False)['country'].count()
# Find the city with the highest count
city_highest_count = city_count.idxmax()
# Print the result
print(city_highest_count)