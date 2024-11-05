import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the 'category' column
automotive_billionaires = df[df['category'] == 'Automotive']
# Filter the dataframe with the 'finalWorth' column
total_worth = automotive_billionaires['finalWorth'].sum()
# Print the result
print(total_worth)