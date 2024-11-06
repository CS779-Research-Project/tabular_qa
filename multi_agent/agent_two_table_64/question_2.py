import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter the dataframe with the column 'aquatic'
aquatic = df['aquatic']
# Filter the dataframe with the column 'backbone'
backbone = df['backbone']
# Count the number of animals that are both aquatic and have a backbone
count = (aquatic & backbone).sum()
# Print the result
print(count)