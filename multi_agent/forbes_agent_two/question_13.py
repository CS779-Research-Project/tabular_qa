import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe to get the youngest billionaire
youngest_billionaire = df[(df['age'] == df['age'].min()) & (df['finalWorth'] > 1e9)]
# Get the source of wealth
source = youngest_billionaire['source'].iloc[0]
# Print the answer
print(f"The source of wealth for the youngest billionaire is: {source}")