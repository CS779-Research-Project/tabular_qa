import pandas as pd
# Load the dataset
df = pd.read_parquet('data/078_SocialMediaUsage.parquet')
# Filter out the rows where 'age' is between 18 and 25
filtered_df = df[(df['age'] >= 18) & (df['age'] <= 25)]
# Filter out the column 'hours_spent' from the filtered dataframe
hours_sp

Here is the output of the code-block present in the above conversation : 
Governor


Observations and Changes Made : 
The code provided does not correctly calculate the average number of hours spent on social media by users aged between 18 and 25. The code attempts to print the 'Governor' value, which is not related to the calculation. Here is the corrected code:

Re-attempted Code with Modifications :
