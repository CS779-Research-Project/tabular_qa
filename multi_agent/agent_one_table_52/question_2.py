import pandas as pd
# Load the dataset
df = pd.read_parquet('data/052_Professional.parquet')
# Filter out the columns 'Profession', 'Emotional_Range', and 'Conversation' from the dataframe
df = df[['Profession', 'Emotional_Range', 'Conversation']]
# Group the dataframe by 'Profession'
grouped = df.groupby('Profession')
# For each profession, find the minimum 'Emotional_Range' and minimum 'Conversation'
min_emotional_range = grouped['Emotional_Range'].min()
min_conversation = grouped['Conversation'].min()
# Check if the profession with the lowest 'Emotional_Range' also has the lowest 'Conversation'
lowest_emotional_range_and_lowest_conversation = (min_emotional_range == min_conversation).any()
# Print the result
print(lowest_emotional_range_and_lowest_conversation)