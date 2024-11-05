import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'finalWorth' and'selfMade' from the dataframe
df = df[['finalWorth','selfMade']]
# Find the person with the highest net worth
highest_net_worth = df['finalWorth'].max()
person = df[df['finalWorth'] == highest_net_worth]
# Check if this person is self-made
is_self_made = person['selfMade'].values[0]
# Print the result
print(is_self_made)