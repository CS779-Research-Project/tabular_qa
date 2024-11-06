import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Profession' and 'Conversation' from the dataframe and sort by 'Conversation' in descending order
df_sorted = df[['Profession', 'Conversation']].sort_values(by='Conversation', ascending=False).head(5)
# Print the result
print(df_sorted['Profession'].tolist())