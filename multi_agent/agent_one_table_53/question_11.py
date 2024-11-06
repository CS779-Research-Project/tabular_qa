import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'graphext_cluster' from the dataframe
cluster = df['graphext_cluster']
# Count the frequency of each cluster
cluster_counts = cluster.value_counts()
# Find the cluster with the highest frequency
most_common_cluster = cluster_counts.idxmax()
# Print the result
print(most_common_cluster)