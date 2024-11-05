import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the rows where 'category' is 'Automotive'
automotive_df = df[df['category'] == 'Automotive']
# Filter out the 'finalWorth' column
final_worth = automotive_df['finalWorth']
# Calculate the total worth
total_worth = final_worth.sum()
# Print the result
print(f"The total worth of billionaires in the 'Automotive' category is: {total_worth}")