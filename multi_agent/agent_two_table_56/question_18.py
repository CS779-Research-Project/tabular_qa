import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the column 'Total Fat (g)' from the dataframe
total_fat = df['Total Fat (g)']
# Sort the dataframe in descending order based on 'Total Fat (g)'
sorted_total_fat = total_fat.sort_values(ascending=False)
# Get the top 4 values
top_4_total_fat = sorted_total_fat.head(4)
# Print the result
print(top_4_total_fat.tolist())