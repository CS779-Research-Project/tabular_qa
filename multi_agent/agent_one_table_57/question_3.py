import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'User self-placement on Left-Right economic values axis' from the dataframe
left_right_axis = df['User self-placement on Left-Right economic values axis']
# Check if any value in the column is equal to 1 (representing extreme right)
extreme_right = left_right_axis.eq(1)
# Print the result
print(extreme_right.any())