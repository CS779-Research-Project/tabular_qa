import pandas as pd
# Load the dataset
df = pd.read_parquet('data/064_Clustering.parquet')
# Filter out the column 'legs' from the dataframe
legs = df['legs']
# Calculate the average number of legs
average_legs = legs.mean()
# Print the result
print(f"The average number of legs is: {average_legs:.2f}")