import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column'make' from the dataframe
make = df['make']
# Get the counts of each make
make_counts = make.value_counts()
# Get the top 5 most prevalent'make' values
top_5_makes = make_counts[:5].index.tolist()
# Print the result
print(top_5_makes)