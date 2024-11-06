import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the column 'legs' from the dataframe
legs = df['legs']
# Count the number of animals with 2 legs
count_two_legs = (legs == 2).sum()
# Print the result
print(count_two_legs)