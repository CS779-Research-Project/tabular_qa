import pandas as pd
# Load the dataset
df = pd.read_parquet('data/055_German.parquet')
# Filter out the column 'Job' from the dataframe
job = df['Job']
# Count the frequency of each job category
job_counts = job.value_counts()
# Find the job category with the highest frequency
most_common_job = job_counts.idxmax()
# Print the result
print(f"The most common job category is '{most_common_job}' with a count of {job_counts[most_common_job]}")