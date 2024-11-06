import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the column 'weight' from the dataframe
weight = df['weight']
# Check if there are any values greater than 500
has_weight_greater_than_500 = weight > 500
# Print the result
print(has_weight_greater_than_500.any())