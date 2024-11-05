import pandas as pd
# Load the dataset
df = pd.read_parquet('data/001_Forbes.parquet')
# Filter out the columns 'philanthropyScore' and 'gender' from the dataframe
df = df[['philanthropyScore', 'gender']]
# Filter the dataframe to get the person with the highest philanthropy score
person_index = df['philanthropyScore'].idxmax()
person = df.loc[person_index]
# Get the gender of the person
gender = person['gender']
# Print the result
print(gender)