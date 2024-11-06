import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Profession' and 'Openness' from the dataframe
profession_openness = df[['Profession', 'Openness']]
# Group the dataframe by 'Profession' and calculate the mean 'Openness' for each profession
mean_openness = profession_openness.groupby('Profession')['Openness'].mean().sort_values(ascending=False)
# Get the top 3 professions with the highest mean 'Openness'
top_3_professions = mean_openness.head(3).index.tolist()
# Print the result
print(top_3_professions)