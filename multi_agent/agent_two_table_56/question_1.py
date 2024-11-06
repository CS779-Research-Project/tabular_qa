import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the column 'Total Sugar (g)' from the dataframe
total_sugar = df['Total Sugar (g)']
# Check if all values in the 'Total Sugar (g)' column are non-zero
all_non_zero = (total_sugar!= 0).all()
# Convert the result to a boolean value
result = bool(all_non_zero)
# Print the result
print(result)