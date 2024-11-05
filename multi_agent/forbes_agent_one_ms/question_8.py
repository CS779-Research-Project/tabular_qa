import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the column 'philanthropyScore' from the dataframe
philanthropy_score = df['philanthropyScore']
# Filter the dataframe to get rows where 'philanthropyScore' is above 3
high_philanthropy_score = philanthropy_score[philanthropy_score > 3]
# Count the number of such rows
num_billionaires = high_philanthropy_score.count()
# Print the result
print(num_billionaires)