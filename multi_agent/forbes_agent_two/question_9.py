import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column'selfMade'
df = df[df['selfMade'] == False]
# Find the maximum rank of the wealthiest non-self-made billionaire
max_rank = df['rank'].idxmax()
# Print the result
print(max_rank)