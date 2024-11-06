import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'User self-placement on Left-Right economic values axis' from the dataframe
left_right_axis = df['User self-placement on Left-Right economic values axis']
# Exclude NaN values
left_right_axis = left_right_axis.dropna()
# Get the frequency of each unique value
value_counts = left_right_axis.value_counts()
# Get the top 3 most common values
top_3_values = value_counts.index[:3].tolist()
# Print the result
print(top_3_values)