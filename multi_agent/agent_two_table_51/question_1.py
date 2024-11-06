import pandas as pd
# Load the dataset
df = pd.read_parquet('data/051_Pokemon.parquet')
# Filter out the columns 'total' and'speed' from the dataframe
total_speed = df[['total','speed']]
# Check if there are any values greater than 700 in the 'total' column
total_greater_than_700 = total_speed['total'] > 700
# Check if there are any values greater than 100 in the'speed' column
speed_greater_than_100 = total_speed['speed'] > 100
# Check if the 'legendary' column is True
legendary = df['legendary']
# Combine the conditions using the & operator
result = (total_greater_than_700 & speed_greater_than_100) & legendary
# Print the result
print(result.any())