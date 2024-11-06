import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Select the 'Quantity' column from the DataFrame
quantity = df['Quantity']
# Calculate the frequency of each unique value in the 'Quantity' column
frequency = quantity.value_counts()
# Extract the indices of the four most common values
top_four_indices = frequency.head(4).index
# Convert these indices to their corresponding values
top_four_quantities = top_four_indices.tolist()
# Print the result
print(top_four_quantities)