import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Extract the 'power' column from the dataframe
power = df['power']
# Sort the power values in descending order
sorted_power = power.sort_values(ascending=False)
# Select the top 6 values
top_6_power = sorted_power.head(6)
# Convert the pandas Series object to a list
top_6_power_list = top_6_power.tolist()
# Print the list of the 6 highest power values
print(top_6_power_list)