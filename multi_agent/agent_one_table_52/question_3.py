import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Openness to Change' and 'Hedonism' from the dataframe
df = df[['Openness to Change', 'Hedonism']]
# Calculate the average level of Openness to Change
average_openness_to_change = df['Openness to Change'].mean()
# Calculate the average level of Hedonism
average_hedonism = df['Hedonism'].mean()
# Compare the two averages and print whether the average level of Openness to Change is higher than the average level of Hedonism
print(average_openness_to_change > average_hedonism)