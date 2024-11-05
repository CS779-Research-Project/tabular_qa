import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'age' and'source' from the dataframe
df = df[['age','source']]
# Filter the dataframe to get the youngest billionaire
youngest_billionaire = df[df['age'] == df['age'].min()]
# Get the source of wealth of the youngest billionaire
source_of_wealth = youngest_billionaire.iloc[0]['source']
# Print the result
print(source_of_wealth)