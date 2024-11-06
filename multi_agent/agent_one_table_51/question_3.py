import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the column'speed' from the dataframe
speed = df['speed']
# Check if there is any value greater than 150
any_speed_greater_than_150 = speed > 150
# Print the result
print(any_speed_greater_than_150)