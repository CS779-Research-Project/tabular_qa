import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the column 'Description' from the dataframe
descriptions = df['Description']
# Count the frequency of each description
description_counts = descriptions.value_counts()
# Get the counts of the two most common descriptions
most_common_counts = description_counts[:2].tolist()
# Print the result
print(most_common_counts)