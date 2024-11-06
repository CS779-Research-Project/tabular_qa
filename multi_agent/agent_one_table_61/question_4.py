import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the column 'Reviewer_Location' from the dataframe
reviewer_location = df['Reviewer_Location']
# Calculate the number of unique reviewer locations
unique_locations = reviewer_location.nunique()
# Print the result
print(unique_locations)