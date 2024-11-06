import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column 'kms' from the dataframe
kms = df['kms']
# Sort the dataframe by 'kms' in descending order
sorted_kms = kms.sort_values(ascending=False)
# Get the top 3 highest mileages
top_3_kms = sorted_kms[:3].tolist()
# Print the result
print(top_3_kms)