import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'State' from the dataframe
states = df['State']
# Get the top 5 unique states
top_5_states = states.value_counts().head(5).index.tolist()
# Print the result
print(top_5_states)