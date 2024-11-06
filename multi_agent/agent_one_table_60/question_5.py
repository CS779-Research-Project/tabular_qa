import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Convert 'date_time' column to datetime format
df['date_time'] = pd.to_datetime(df['date_time'])
# Filter out the column 'date_time' from the dataframe
date_time = df['date_time']
# Count the unique dates
unique_dates = date_time.nunique()
# Print the result
print(unique_dates)