import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column 'fuel' from the dataframe
fuel = df['fuel']
# Get the unique values of the 'fuel' column
unique_fuel = fuel.unique()
# Sort the unique values by their count in ascending order
fuel_counts = fuel.value_counts().sort_values()
# Get the first two values
least_common_fuels = unique_fuel[fuel_counts.index[:2]]
# Print the result
print(least_common_fuels.tolist())