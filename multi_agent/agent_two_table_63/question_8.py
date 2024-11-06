import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Find the most common name
most_common_name = df['name'].mode()[0]
# Print the result
print(most_common_name)