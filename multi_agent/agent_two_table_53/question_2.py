import pandas as pd
# Load the dataset
df = pd.read_parquet('data/053_Patents.parquet')
# Filter out the column 'abstract' from the dataframe
abstracts = df['abstract']
# Check if the word'software' is mentioned in the abstract
mentions_software = abstracts.str.contains('software', case=False, na=False)
# Print the result
print(mentions_software.any())