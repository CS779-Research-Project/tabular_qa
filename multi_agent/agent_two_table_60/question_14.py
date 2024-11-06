import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')

# Filter out the columns 'Item' and 'weekday_weekend' from the dataframe
df = df[['Item', 'weekday_weekend']]

# Filter the dataframe to get the rows where 'weekday_weekend' is 'weekend'
weekend_sales = df[df['weekday_weekend'] == 'weekend']

# Group the dataframe by 'Item' and count the number of occurrences
item_counts = weekend_sales.groupby('Item').size()

# Sort the grouped dataframe by count in descending order and then by 'Item' in ascending order
sorted_item_counts = item_counts.sort_values(ascending=False).reset_index(name='count')

# Get the top 2 items
top_items = sorted_item_counts.head(2)

# Print the result
print(top_items['Item'].tolist())