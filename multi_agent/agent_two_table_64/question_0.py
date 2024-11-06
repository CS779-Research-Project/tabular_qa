import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the column 'feathers' from the dataframe
feathers = df['feathers']
# Check if there are any non-zero values in the 'feathers' column
has_feathers = feathers.any()
# Print the result
print(has_feathers)