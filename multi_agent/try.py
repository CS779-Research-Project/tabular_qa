import pandas as pd

# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')

# Filter the dataframe with the column 'rank'
rank = df['rank']

# Filter the dataframe with the column'selfMade'
selfMade = df['selfMade']

# Check if the filtered dataframe has any non-self-made billionaires in the top 5 ranks
non_self_made_billionaires = rank.isin([1, 2, 3, 4, 5]) & selfMade.isin([False])

# Print the result
print(non_self_made_billionaires)