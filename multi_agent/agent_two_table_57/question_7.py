import pandas as pd
# Load the dataset
df = pd.read_parquet('data/057_Spain.parquet')
# Filter the dataframe with the column 'gender' where the value is 'None'
df_no_gender = df[df['gender'] == 'None']
# Get the maximum age among the respondents who prefer not to disclose their gender
max_age = df_no_gender['Age'].max()
# Print the result
print(max_age)