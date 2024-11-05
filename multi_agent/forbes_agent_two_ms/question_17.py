import pandas as pd
# Load the dataset
df = pd.read_parquet('data/002_HealthData.parquet')
# Filter out the rows where

Here is the output of the code-block present in the above conversation : 
[nan, 'Oslo', 'Jiaozuo', 'Los Angeles']


Observations and Changes Made:
1. The code does not filter the rows based on 'bmi' and 'gender' conditions.
2. The code does not calculate the average of 'exercise_hours_per_week'.
3. The code incorrectly prints the 'city' column instead of the average 'exercise_hours_per_week'.

Re-attempted Code with Modifications:
