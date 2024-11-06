import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Sort the dataframe by 'weight' in descending order and get the top 3 rows
top_3 = df.sort_values(by='weight', ascending=False).head(3)[['name']]
# Convert the result to a list
names_list = top_3['name'].tolist()
# Print the result
print(names_list)