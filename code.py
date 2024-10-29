import pandas as pd

# Load the dataset and filter out the 'Quantity' column
df = pd.read_parquet("hf://datasets/cardiffnlp/databench/data/065_RFM/all.parquet")
quantities = df['Quantity']

# Count the occurrences of each unique quantity
quantity_counts = quantities.value_counts()

# Sort the quantities in ascending order based on their counts
sorted_quantities = quantity_counts.sort_values()

# Extract the three least common quantities
three_least_common_quantities = sorted_quantities.head(3).index.tolist()

# Return the list of the three least commonly ordered quantities
print(three_least_common_quantities)