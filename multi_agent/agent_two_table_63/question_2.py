import pandas as pd
# Load the dataset
df = pd.read_parquet('data/063_Influencers.parquet')
# Filter out the column 'pic' from the dataframe
pics = df['pic']
# Check if all values in the 'pic' column are not null
all_pics_exist = pics.notnull().all()
# Print the result
print(all_pics_exist)