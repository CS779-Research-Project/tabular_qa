import pandas as pd
df = pd.read_parquet('data/061_Disneyland.parquet')
df = df[['Reviewer_Location', 'Rating']]
grouped_df = df.groupby

Here is the output of the code-block present in the above conversation : 
<string>:7: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
False


Re-attempted Code with Modifications : 
