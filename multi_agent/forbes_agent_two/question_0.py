import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'finalWorth'
df_highest_net_worth = df[df['finalWorth'] == df['finalWorth'].max()]
# Check if the person with the highest net worth is self-made
is_self_made = df_highest_net_worth['selfMade'].iloc[0]
# Print the result
print(is_self_made)