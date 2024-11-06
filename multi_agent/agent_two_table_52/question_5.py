import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter the dataframe to get the professions with Emotional_Range above 0.5
num_professions = len(df[df['Emotional_Range'] > 0.5])
# Print the result
print(num_professions)