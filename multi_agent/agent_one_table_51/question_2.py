import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the columns 'generation' and 'legendary' from the dataframe
df = df[['generation', 'legendary']]
# Check if all values in 'legendary' column are True
all_legendary = df['legendary'].all()
# Print the result
print(all_legendary)