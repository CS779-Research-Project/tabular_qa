import pandas as pd
# Load the dataset
df = pd.read_parquet('data/065_RFM.parquet')
# Filter out the column 'CustomerID' from the dataframe
customer_id = df['CustomerID']
# Check for missing values in the 'CustomerID' column
missing_customer_ids = customer_id.isnull().any()
# Convert the result to a boolean value
missing_customer_ids_bool = bool(missing_customer_ids)
# Print the result
print(missing_customer_ids_bool)