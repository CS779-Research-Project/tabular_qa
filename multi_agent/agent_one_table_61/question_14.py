import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Count the number of reviews for each date and get the top 4 dates with the most reviews
top_4_dates = df['Year_Month'].value_counts().head(4).index.tolist()
# Print the result
print(top_4_dates)