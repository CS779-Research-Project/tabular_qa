import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Get the bottom 3 weights directly
bottom_3_weights = df['weight'].nsmallest(3)
# Print the result
print(bottom_3_weights.tolist())