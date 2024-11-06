import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter the dataframe with the column 'Region'
region = df['Region']
# Count the number of respondents from the 'Northeast' region
northeast_respondents = region.value_counts()['Northeast']
# Print the result
print(northeast_respondents)