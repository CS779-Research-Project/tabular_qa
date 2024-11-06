# Step 1: Load the dataset
import pandas as pd
df = pd.read_parquet('data/053_Patents.parquet')

# Step 2: Filter out the column 'type' from the dataframe
type_column = df['type']

# Step 3: Count the number of 'utility' patents
utility_patents = (type_column == 'utility').sum()

# Step 4: Print the result
print(utility_patents)