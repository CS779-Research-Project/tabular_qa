import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Count the frequency of each unique value in the 'partyId' column and find the most common value
most_common_partyId = df['partyId'].value_counts().idxmax()
# Print the result
print(most_common_partyId)