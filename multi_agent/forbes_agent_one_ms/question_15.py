import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the column 'country' from the dataframe
countries = df['country']
# Group the dataframe by 'country' and count the number of occurrences
country_counts = countries.value_counts()
# Sort the grouped dataframe by the count in descending order
country_counts_sorted = country_counts.sort_values(ascending=False)
# Get the top 3 countries
top_3_countries = country_counts_sorted.head(3).index.tolist()
# Print the result
print(top_3_countries)