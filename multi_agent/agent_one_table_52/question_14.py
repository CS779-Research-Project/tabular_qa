import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Profession' and 'Conversation' from the dataframe
df = df[['Profession', 'Conversation']]
# Sort the dataframe by 'Conversation' in descending order
df_sorted = df.sort_values(by='Conversation', ascending=False)
# Get the top 5 professions
top_5_professions = df_sorted['Profession'].head(5)
# Print the result
print(top_5_professions.tolist())