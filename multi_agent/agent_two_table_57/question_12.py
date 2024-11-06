import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'Vote Intention' from the dataframe
vote_intention = df['Vote Intention']
# Count the frequency of each unique value in the 'Vote Intention' column
vote_intention_counts = vote_intention.value_counts()
# Sort the unique values by their frequency in descending order
top_vote_intentions = vote_intention_counts.sort_values(ascending=False)
# Get the top 5 most common vote intentions
top_5_vote_intentions = top_vote_intentions[:5].index.tolist()
# Print the result
print(top_5_vote_intentions)