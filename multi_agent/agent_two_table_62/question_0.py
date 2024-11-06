import pandas as pd
# Load the dataset
df = pd.read_parquet('data/062_Trump.parquet')
# Check if all the values in the 'lang' column are 'en'
all_english = df['lang'].nunique() == 1
# Print the result
print(all_english)