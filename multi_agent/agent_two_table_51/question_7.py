import pandas as pd

# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')

# Filter out the 'attack' column from the DataFrame
attack = df['attack']

# Calculate the average attack
average_attack = attack.mean()

# Print the result
print(average_attack)