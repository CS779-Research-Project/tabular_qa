import pandas as pd
from collections import Counter
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the column 'legs' from the dataframe
legs = df['legs']
# Count the frequency of each unique value in the 'legs' column
legs_counts = Counter(legs)
# Get the least common 3 numbers of legs
least_common_legs = legs_counts.most_common()[:-4:-1]
# Print the result
print(least_common_legs)