import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'Item' and 'period_day' from the dataframe
df = df[['Item', 'period_day']]
# Filter the dataframe to get the items purchased during the afternoon
afternoon_purchases = df[df['period_day'] == 'afternoon']
# Get the top 2 most purchased items
top_2_items = afternoon_purchases['Item'].value_counts().index[:2].tolist()
# Print the result
print(top_2_items)