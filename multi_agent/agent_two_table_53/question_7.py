# No modifications needed, the code is correct as provided
import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'type' from the dataframe
type_column = df['type']
# Count the number of 'utility' patents
utility_patents = (type_column == 'utility').sum()
# Print the result
print(utility_patents)