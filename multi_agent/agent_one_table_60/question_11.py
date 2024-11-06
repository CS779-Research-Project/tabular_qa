import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'Item' and 'period_day' from the dataframe
df = df[['Item', 'period_day']]
# Group the dataframe by 'period_day'
grouped_df = df.groupby('period_day')
# Count the number of occurrences for each period_day
counts = grouped_df['period_day'].count()
# Find the period_day with the highest count
most_frequent_period = counts.idxmax()
# Print the result
print(most_frequent_period)