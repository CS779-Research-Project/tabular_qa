import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column 'fuel' from the dataframe
fuel = df['fuel']
# Get the count of each unique fuel type
fuel_counts = fuel.value_counts()
# Sort the fuel types by their count in ascending order
least_common_fuels = fuel_counts.sort_values().index[:2]
# Convert the result to a list and print it
print(least_common_fuels.tolist())