# Step 1: Load the dataset
import pandas as pd
df = pd.read_parquet('data/057_Spain.parquet')

# Step 2: Filter out the column 'Vote Intention' from the dataframe
vote_intention = df['Vote Intention']

# Step 3: Count the frequency of each category in the 'Vote Intention' column
vote_intention_counts = vote_intention.value_counts()

# Step 4: Find the category with the highest frequency
most_common_vote_intention = vote_intention_counts.idxmax()

# Step 5: Print the result
print(most_common_vote_intention)