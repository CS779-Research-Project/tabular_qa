import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Select the 'Self-enhancement' column
self_enhancement = df['Self-enhancement']
# Find the maximum value in the 'Self-enhancement' column
max_self_enhancement = self_enhancement.max()
# Print the maximum value of 'Self-enhancement'
print(max_self_enhancement)