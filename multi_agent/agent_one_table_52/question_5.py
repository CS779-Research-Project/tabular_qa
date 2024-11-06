import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the column 'Emotional_Range' from the dataframe
emotional_range = df['Emotional_Range']
# Filter the dataframe to get the professions with Emotional_Range above 0.5
professions = df[emotional_range > 0.5]
# Count the number of professions
num_professions = len(professions)
# Print the result
print(num_professions)