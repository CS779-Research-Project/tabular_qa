import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'Division' from the dataframe
division = df['Division']
# Count the number of unique values in the 'Division' column
unique_divisions = division.nunique()
# Convert the unique_divisions to a pandas Series
unique_divisions_series = pd.Series(unique_divisions)
# Filter the count to get the count of regions adjacent to the South Atlantic Ocean
south_atlantic_ocean_count = unique_divisions_series['South Atlantic Ocean']
# Print the result
print(south_atlantic_ocean_count)