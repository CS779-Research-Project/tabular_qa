import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Count the frequency of each unique value in the 'partyId' column
party_counts = df['partyId'].value_counts()
# Sort the counts in descending order
party_counts_sorted = party_counts.sort_values(ascending=False)
# Get the top 4 most common party identifications
top_4_parties = party_counts_sorted[:4].index.tolist()
# Print the result
print(top_4_parties)