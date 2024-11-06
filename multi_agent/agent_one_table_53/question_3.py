import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'type' from the dataframe
type_column = df['type']
# Check if there are any 'design' patents
design_patents = type_column == 'design'
# Print the result
print(design_patents.any())