import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Get the frequency of each unique value in the 'kind' column
kind_frequency = df['kind'].value_counts().sort_values(ascending=False)
# Get the top 5 most frequent values
top_5_kinds = kind_frequency.index[:5].tolist()
# Print the result
print(top_5_kinds)