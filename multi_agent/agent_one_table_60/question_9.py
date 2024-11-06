import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'Item' and 'weekday_weekend' from the dataframe
df = df[['Item', 'weekday_weekend']]
# Filter the dataframe to get the rows where 'weekday_weekend' is 'weekday'
weekday_df = df[df['weekday_weekend'] == 'weekday']
# Count the frequency of each 'Item'
item_counts = weekday_df['Item'].value_counts()
# Find the 'Item' with the highest frequency
most_common_item = item_counts.idxmax()
# Print the result
print(most_common_item)