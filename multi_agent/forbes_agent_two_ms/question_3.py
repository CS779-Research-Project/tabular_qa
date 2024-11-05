import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'rank' and'selfMade' from the dataframe
df = df[['rank','selfMade']]
# Check if there is a non-self-made billionaire in the top 5 ranks
non_self_made_billionaire = df[(df['rank'] <= 5) & (~df['selfMade'])]
# Print the result
print(len(non_self_made_billionaire) > 0)