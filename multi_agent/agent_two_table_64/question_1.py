import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the column'venomous' from the dataframe
venomous = df['venomous']
# Check if there are any True values in the'venomous' column
has_venomous = venomous.any()
# Print the result
print(has_venomous)