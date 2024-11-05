import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'philanthropyScore'
philanthropy_score = df[df['philanthropyScore'] > 3]
# Count the number of billionaires with a philanthropy score above 3
count = philanthropy_score.shape[0]
# Print the result
print(count)