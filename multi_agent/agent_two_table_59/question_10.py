import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column 'fuel' from the dataframe
fuel = df['fuel']
# Count the frequency of each unique value in the 'fuel' column
fuel_counts = fuel.value_counts()
# Find the most common fuel
most_common_fuel = fuel_counts.idxmax()
# Print the result
print(f"The most common fuel is {most_common_fuel} with a count of {fuel_counts[most_common_fuel]}")