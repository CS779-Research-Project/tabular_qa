import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter the dataframe to get the billionaire with the lowest rank and get the title
billionaire = df[df['rank'] == df['rank'].min()]['title'].iloc[0]
# Print the result
print(billionaire)