import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'Item' and 'weekday_weekend' from the dataframe
df = df[['Item', 'weekday_weekend']]
# Group the dataframe by 'weekday_weekend'
grouped = df.groupby('weekday_weekend')
# Count the number of occurrences of each item for weekdays
counts = grouped['Item'].value_counts()
# Find the item with the least occurrences
least_popular_item = counts.idxmin()
# Print the result
print(least_popular_item)