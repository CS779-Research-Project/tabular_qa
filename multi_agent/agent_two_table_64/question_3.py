import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the column 'domestic' from the dataframe
domestic = df['domestic']
# Check if there are any True values in the column
has_domestic = domestic.any()
# Print the result
print(has_domestic)