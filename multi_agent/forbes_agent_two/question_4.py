import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe with the column 'age'
oldest_billionaire = df[df['age'] == df['age'].max()]
# Check if the philanthropy score of the oldest billionaire is 5
is_billionaire_with_philanthropy_score_5 = oldest_billionaire['philanthropyScore'].max() == 5
# Print the result
print(is_billionaire_with_philanthropy_score_5)