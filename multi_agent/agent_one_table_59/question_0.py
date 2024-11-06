import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column'model' from the dataframe
models = df['model']
# Get the unique values in the'model' column
unique_models = models.unique()
# Count the number of unique values
num_unique_models = len(unique_models)
# Print the result
print(num_unique_models)