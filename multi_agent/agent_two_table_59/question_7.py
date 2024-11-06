import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column 'year' from the dataframe
year = df['year']
# Filter the dataframe to get the cars from the year 2020
cars_from_2020 = year[year == 2020]
# Count the number of cars from the year 2020
count = cars_from_2020.count()
# Print the result
print(count)