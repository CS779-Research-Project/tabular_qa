import pandas as pd
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Count the frequency of each unique value in the 'type' column and find the most common value
most_common_type = df['type'].value_counts().idxmax()
# Print the result
print(most_common_type)