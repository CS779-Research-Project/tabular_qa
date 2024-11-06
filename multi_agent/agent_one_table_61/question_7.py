import pandas as pd
# Load the dataset
df = pd.read_parquet('data/061_Disneyland.parquet')
# Filter out the column 'Year_Month' from the dataframe
year_month = df['Year_Month']
# Filter the dataframe to get the reviews made in 2019
reviews_in_2019 = year_month[year_month == '2019']
# Count the number of reviews
number_of_reviews = reviews_in_2019.count()
# Print the result
print(number_of_reviews)