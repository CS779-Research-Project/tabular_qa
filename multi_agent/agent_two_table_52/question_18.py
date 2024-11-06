import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the column 'Extraversion' from the dataframe
extraversion = df['Extraversion']
# Sort the dataframe by 'Extraversion' in descending order
extraversion_sorted = extraversion.sort_values(ascending=False)
# Get the top 5 levels of 'Extraversion'
top_5_extraversion = extraversion_sorted.head(5).tolist()
# Print the result
print(top_5_extraversion)