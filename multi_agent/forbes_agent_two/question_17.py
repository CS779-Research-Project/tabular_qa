import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'city'
city = df['city']
# Sort the dataframe by 'age' in ascending order
sorted_df = df.sort_values(by=['age'], ascending=True)
# Select the top 4 rows
top_4_cities = sorted_df.head(4)
# Print the result as a list of categories
print(top_4_cities['city'].tolist())