import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Select the 'Age' column from the DataFrame
age = df['Age']
# Get the frequency of each age
age_counts = age.value_counts()
# Get the top 5 most common ages
top_5_ages = age_counts.nlargest(5)
# Convert the index to a list
top_5_ages_list = top_5_ages.index.tolist()
# Print the result
print(top_5_ages_list)