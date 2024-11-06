import pandas as pd
# Load the dataset
df = pd.read_parquet('data/060_Bakery.parquet')
# Filter out the column 'period_day' from the dataframe
period_day = df['period_day']
# Check if there are any 'night' values in the 'period_day' column
night_transactions = period_day.str.contains('night').any()
# Print the result
print(night_transactions)