import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the column 'Sodium (g)' from the dataframe
sodium = df['Sodium (g)']
# Filter the dataframe to get the rows where 'Sodium (g)' is more than 1
high_sodium = sodium[sodium > 1]
# Count the number of rows
count = high_sodium.count()
# Print the result
print(count)