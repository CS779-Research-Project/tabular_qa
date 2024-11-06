import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'User self- placement on Progressive-Conservative economic values axis' from the dataframe
progressive_conservative_axis = df['User self- placement on Progressive-Conservative economic values axis']
# Count the number of respondents who placed themselves at 10 on the Progressive-Conservative economic values axis
count_at_ten = (progressive_conservative_axis == 10).sum()
# Print the result
print(count_at_ten)