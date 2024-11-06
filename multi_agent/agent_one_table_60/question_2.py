import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'Item' and 'weekday_weekend' from the dataframe
df = df[['Item', 'weekday_weekend']]
# Check if all unique values in 'weekday_weekend' column are 'weekday'
all_weekdays = df['weekday_weekend'].nunique() == 1
# Print the result
print(all_weekdays)