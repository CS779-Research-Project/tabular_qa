import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the column 'Reviewer_Location' from the dataframe
reviewer_location = df['Reviewer_Location']
# Calculate the most common reviewer location
most_common_location = reviewer_location.mode()[0]
# Print the result
print(f"The most common reviewer location is: {most_common_location}")