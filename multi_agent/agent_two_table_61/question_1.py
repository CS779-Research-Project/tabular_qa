import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Extract the unique values from the 'Branch' column
branches = df['Branch'].unique()
# Check if 'Disneyland_HongKong' is among the unique branch values
is_most_reviewed = 'Disneyland_HongKong' in branches
# Convert the result to a boolean value
is_most_reviewed_bool = bool(is_most_reviewed)
# Print the result
print(is_most_reviewed_bool)