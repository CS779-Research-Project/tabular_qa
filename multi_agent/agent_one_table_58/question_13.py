import pandas as pd
# Load the dataset
df = pd.read_parquet('data/058_US.parquet')
# Filter out the column 'Which of these best describes the kind of work you do?' from the dataframe
work_type = df['Which of these best describes the kind of work you do?']
# Count the frequency of each category
work_type_counts = work_type.value_counts()
# Get the top 4 most common categories
top_4_work_types = work_type_counts.head(4)
# Print the result
print(top_4_work_types.index.tolist())