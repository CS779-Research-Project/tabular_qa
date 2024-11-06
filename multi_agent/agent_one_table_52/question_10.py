import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Profession' and 'Emotional_Range' from the dataframe
df = df[['Profession', 'Emotional_Range']]
# Group the dataframe by 'Profession' and calculate the mean 'Emotional_Range' for each profession
mean_emotional_range = df.groupby('Profession')['Emotional_Range'].mean()
# Find the profession with the highest mean 'Emotional_Range'
highest_emotional_range_profession = mean_emotional_range.idxmax()
# Print the result
print(highest_emotional_range_profession)