import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Select the 'polInterest' column
polInterest = df['polInterest']
# Convert 'polInterest' column to boolean type
polInterest_bool = polInterest.astype(bool)
# Check if all values are True
all_interested = polInterest_bool.all()
# Print the result
print(all_interested)