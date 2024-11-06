import pandas as pd

# Load the dataset
df = pd.read_parquet('data/058_US.parquet')

# Filter out the 'likelihood' column from the dataframe
likelihood = df['likelihood']

# Count the frequency of each unique value in the 'likelihood' column
frequency = likelihood.value_counts()

# Sort the frequency count in descending order
sorted_frequency = frequency.sort_values(ascending=False)

# Get the top 6 most common likelihood values
top_6_likelihood = sorted_frequency.head(6)

# Print the result
print(top_6_likelihood)