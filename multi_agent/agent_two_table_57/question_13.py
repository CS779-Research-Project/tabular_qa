import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'voteReason' from the dataframe
vote_reason = df['voteReason']
# Count the frequency of each unique value in the 'voteReason' column
vote_reason_counts = vote_reason.value_counts()
# Sort the unique values by their frequency in descending order
top_3_vote_reasons = vote_reason_counts.nlargest(3)
# Get the top 3 most common reasons
top_3_vote_reasons_list = top_3_vote_reasons.index.tolist()
# Print the result
print(top_3_vote_reasons_list)