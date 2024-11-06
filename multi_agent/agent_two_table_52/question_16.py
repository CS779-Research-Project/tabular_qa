import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Group the dataframe by 'Profession'
grouped = df.groupby('Profession')
# Calculate the average 'Openness to Change' for each profession
average_openness = grouped['Openness to Change'].mean()
# Sort the professions by the average 'Openness to Change' in descending order
sorted_professions = average_openness.sort_values(ascending=False)
# Get the top 3 professions
top_3_professions = sorted_professions.head(3)
# For each of these professions, get the average Openness to Change
result = [(profession, average_openness[profession]) for profession in top_3_professions.index]
# Print the result
print(result)