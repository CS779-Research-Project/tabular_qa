import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the column 'Openness to Change' from the dataframe
openness_to_change = df['Openness to Change']
# Sort the values in the 'Openness to Change' column in descending order
sorted_openness = openness_to_change.sort_values(ascending=False)
# Get the top 3 values
top_3_openness = sorted_openness.head(3)
# Print the result
print(top_3_openness.tolist())