import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Select the 'community' column
communities = df['community']
# Count the number of unique communities
num_unique_communities = communities.nunique()
# Print the result
print(num_unique_communities)