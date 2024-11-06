import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Select the 'polInterest' column
polInterest = df['polInterest']
# Check if all values are True
all_interested = polInterest.all()
# Print the result
print(all_interested)