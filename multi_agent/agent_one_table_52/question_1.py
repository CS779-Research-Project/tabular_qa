import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Profession', 'Openness', and 'Conscientousness' from the dataframe
df = df[['Profession', 'Openness', 'Conscientousness']]
# Group the dataframe by 'Profession'
grouped = df.groupby('Profession')
# For each profession, find the maximum 'Openness' and 'Conscientousness'
max_openness = grouped['Openness'].max()
max_conscientousness = grouped['Conscientousness'].max()
# Check if the profession with the highest 'Openness' has the same 'Conscientousness' as the profession with the highest 'Conscientousness'
same_profession = max_openness.idxmax() == max_conscientousness.idxmax()
# Print the result
print(same_profession)