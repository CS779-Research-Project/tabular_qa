import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'Item' and 'period_day' from the dataframe
df = df[['Item', 'period_day']]
# Filter the dataframe to get the rows where 'period_day' is 'evening'
evening_df = df[df['period_day'] == 'evening']
# Group the filtered dataframe by 'Item' and count the occurrences of each item
item_counts = evening_df.groupby('Item').size()
# Filter the grouped dataframe to get the items that were bought two times
items_bought_twice = item_counts[item_counts == 2].index.tolist()
# Print the result
print(items_bought_twice)