import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'Division' from the dataframe
division = df['Division']
# Count the occurrences of each division
division_counts = division.value_counts()
# Find the division with the greatest representation
greatest_representation = division_counts.idxmax()
# Print the result
print(greatest_representation)