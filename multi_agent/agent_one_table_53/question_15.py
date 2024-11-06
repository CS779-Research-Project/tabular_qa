import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'graphext_cluster' from the dataframe
graphext_cluster = df['graphext_cluster']
# Count the frequency of each cluster
cluster_counts = graphext_cluster.value_counts()
# Identify the 2 least common clusters
least_common_clusters = cluster_counts.nsmallest(2).index.tolist()
# Print the result
print(least_common_clusters)