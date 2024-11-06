import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the column 'Review_ID' from the dataframe
review_id = df['Review_ID']
# Find the maximum review ID
max_review_id = review_id.max()
# Print the result
print(max_review_id)