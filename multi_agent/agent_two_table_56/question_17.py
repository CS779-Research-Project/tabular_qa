import pandas as pd
# Load the dataset
df = pd.read_parquet('data/056_Emoji.parquet')
# Filter out the column 'Total Sugar (g)' from the dataframe
sugar = df['Total Sugar (g)']
# Sort the values in the 'Total Sugar (g)' column in ascending order
sugar_sorted = sugar.sort_values()
# Get the first 3 values
top_3_sugar = sugar_sorted.head(3)
# Convert the result to a list
top_3_sugar_list = top_3_sugar.tolist()
# Print the result
print(f"The 3 lowest amounts of sugar found among the foods are: {top_3_sugar_list}")