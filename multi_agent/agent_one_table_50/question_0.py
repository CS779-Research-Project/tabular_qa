import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns 'favorites' and 'lang' from the dataframe
df = df[['favorites', 'lang']]
# Group the dataframe by 'lang'
grouped = df.groupby('lang')
# Count the number of favorites for each language
favorites_count = grouped['favorites'].sum()
# Check if the language with the most favorites is Spanish
is_spanish = favorites_count.idxmax() == 'Spanish'
# Print the result
print(is_spanish)