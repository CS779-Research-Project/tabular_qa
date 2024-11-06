import pandas as pd
# Load the dataset
df = pd.read_parquet('data/090_Employees.parquet')
# Filter out the columns 'salary' and 'performance_rating' from the dataframe
df = df[['salary', 'performance_rating']]
# Filter the dataframe to get the employee with the highest performance rating
highest_performance_rating = df['performance_rating'].max()
employee = df[df['performance_rating'] == highest_performance_rating]
# Get the salary of the employee
salary = employee['salary']
# Print the result
print(salary)