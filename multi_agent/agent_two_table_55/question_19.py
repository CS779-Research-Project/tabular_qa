import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the column 'Age' from the dataframe
age = df['Age']
# Sort the dataframe by 'Age' in descending order
sorted_age = age.sort_values(ascending=False)
# Get the top 2 oldest ages
top_2_oldest_ages = sorted_age.head(2).tolist()
# Print the result
print(top_2_oldest_ages)