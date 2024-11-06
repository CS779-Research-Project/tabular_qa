import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column 'dealer' from the dataframe
dealers = df['dealer']
# Check if 'Autos Raymara' is in the filtered column
is_associated = 'Autos Raymara' in dealers.values
# Print the result
print(is_associated)