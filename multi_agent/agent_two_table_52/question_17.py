import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the column 'Emotional_Range' from the dataframe
emotional_range = df['Emotional_Range']
# Sort the 'Emotional_Range' values in ascending order
sorted_emotional_range = emotional_range.sort_values().tolist()
# Select the first four values
bottom_4_emotional_range = sorted_emotional_range[:4]
# Print the result
print(bottom_4_emotional_range)