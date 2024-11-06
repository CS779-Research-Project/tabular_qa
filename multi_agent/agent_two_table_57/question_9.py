import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter out the column 'voteReason' from the dataframe
vote_reason = df['voteReason']
# Count the frequency of each unique value in the 'voteReason' column
vote_reason_counts = vote_reason.value_counts()
# Get the most common reason
most_common_reason = vote_reason_counts.idxmax()
# Print the result
print(f"The most common reason for voting is: {most_common_reason}")