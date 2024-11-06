import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the column 'Age' from the dataframe
age = df['Age']
# Filter the dataframe to get the rows where 'Age' is greater than 50
older_than_50 = age[age > 50]
# Count the number of such rows
count = len(older_than_50)
# Print the result
print(count)