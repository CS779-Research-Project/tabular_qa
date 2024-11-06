import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the column 'type1' from the dataframe
type1 = df['type1']
# Count the number of occurrences of 'Fire' in the list of type1
fire_count = (type1 == 'Fire').sum()
# Print the result
print(fire_count)