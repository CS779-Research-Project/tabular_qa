import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column'version' from the dataframe
versions = df['version']
# Check if 'BMW' is mentioned in the'version' column
has_bmw = 'BMW' in versions.values
# Print the result
print(has_bmw)