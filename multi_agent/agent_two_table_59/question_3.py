import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column'shift' from the dataframe
shift = df['shift']
# Check if 'Manual' is in the'shift' column
has_manual = shift.isin(['Manual']).any()
# Print the result
print(has_manual)