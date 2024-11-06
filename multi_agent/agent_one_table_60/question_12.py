import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'Item' and 'period_day' from the dataframe
df = df[['Item', 'period_day']]
# Group the dataframe by 'period_day' and 'Item'
grouped_df = df.groupby(['period_day', 'Item']).size().reset_index(name='counts')
# Count the frequency of each item for each period_day
# Filter the dataframe to get the top 3 items most frequently bought in the morning
morning_df = grouped_df[grouped_df['period_day'] =='morning']
top_3_items = morning_df.sort_values('counts', ascending=False).head(3)['Item'].tolist()
# Print the result
print(top_3_items)