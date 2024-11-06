import pandas as pd
# Load the dataset
df = pd.read_parquet('data/059_Second.parquet')
# Filter out the column'model' from the dataframe
models = df['model']
# Count the unique car models
unique_models = models.nunique()
# Print the result
print(f"Number of unique car models: {unique_models}")