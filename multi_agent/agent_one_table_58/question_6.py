# Filter the dataframe to get the rows where the highest degree or level of school is 'High School' or less
high_school_or_less = education.isin(['High School', 'Some college, no degree'])