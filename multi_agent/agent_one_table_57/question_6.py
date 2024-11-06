import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'It should be more difficult for companies to lay off workers' from the dataframe
difficulty_to_lay_off = df['It should be more difficult for companies to lay off workers']
# Count the number of '1's in the filtered column
count = difficulty_to_lay_off.value_counts()[1]
# Print the result
print(count)