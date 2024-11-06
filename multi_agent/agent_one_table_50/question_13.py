import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns 'lang' and 'favorites' from the dataframe
df = df[['lang', 'favorites']]
# Sort the dataframe by 'favorites' in ascending order
df = df.sort_values(by='favorites')
# Select the top 5 rows
top_5_rows = df.head(5)
# Extract the 'lang' column from these rows
languages = top_5_rows['lang'].tolist()
# Print the result
print(languages)