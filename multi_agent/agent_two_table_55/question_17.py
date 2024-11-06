import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the columns 'Number of Dependants' and 'Risk' from the dataframe
dependants = df['Number of Dependants']
risk = df['Risk']
# Filter the dataframe to get the rows where 'Risk' is 'High'
high_risk_df = df[(risk == 'High')]
# Calculate the average number of dependants for loans with a risk rating of 'High'
average_dependants = high_risk_df['Number of Dependants'].mean()
# Print the result
print(average_dependants)