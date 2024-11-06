import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Profession' and 'Hedonism' from the dataframe
df = df[['Profession', 'Hedonism']]
# Find the profession with the lowest level of Hedonism
lowest_hedonism = df.loc[df['Hedonism'].idxmin()]['Profession']
# Print the result
print(lowest_hedonism)