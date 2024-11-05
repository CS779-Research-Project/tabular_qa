import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'age' and 'city' from the dataframe
df = df[['age', 'city']]
# Sort the dataframe by 'age' in ascending order
df = df.sort_values(by='age')
# Get the top 4 cities
top_4_cities = df['city'].head(4).tolist()
# Print the result
print(top_4_cities)