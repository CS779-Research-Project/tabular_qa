import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'country'
countries = df['country']
# Get the top 3 countries
top_3_countries = countries.value_counts().nlargest(3)
# Print the result
print(top_3_countries.index.tolist())