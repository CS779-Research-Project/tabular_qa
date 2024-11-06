import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Calculate the number of unique reviewer locations
unique_locations = df['Reviewer_Location'].nunique()
# Print the result
print(unique_locations)