import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter the dataframe to get the reviews made in 2019
reviews_in_2019 = df[df['Year_Month'].str.contains('2019')]
# Count the number of reviews
number_of_reviews = reviews_in_2019['Year_Month'].value_counts().iloc[0]
# Print the result
print(number_of_reviews)