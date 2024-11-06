import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column 'year' from the dataframe
years = df['year']
# Count the frequency of each year
year_counts = years.value_counts()
# Get the 4 most common years
most_common_years = year_counts[:4].index.tolist()
# Print the result
print(most_common_years)