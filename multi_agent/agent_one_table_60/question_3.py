import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the columns 'period_day' and 'weekday_weekend' from the dataframe
df = df[['period_day', 'weekday_weekend']]
# Filter the dataframe to get the rows where 'period_day' is 'Evening' and 'weekday_weekend' is True
evening_weekend_transactions = df[(df['period_day'] == 'Evening') & (df['weekday_weekend'] == True)]
# Check if there are any rows that meet the criteria
if not evening_weekend_transactions.empty:
    # Print the result
    print(True)
else:
    # Print the result
    print(False)