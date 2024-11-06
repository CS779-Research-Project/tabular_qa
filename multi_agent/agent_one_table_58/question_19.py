   import pandas as pd
   df = pd.read_parquet('data/058_US.parquet')
   ```
3. Filter out the 'likelihood' column from the dataframe
   ```python
   likelihood = df['likelihood']
   ```
4. Count the frequency of each unique value in the 'likelihood' column
   ```python
   frequency = likelihood.value_counts()
   ```
5. Sort the frequency count in descending order
   ```python
   sorted_frequency = frequency.sort_values(ascending=False)
   ```
6. Get the top 6 most common likelihood values
   ```python
   top_6_likelihood = sorted_frequency.head(6)
   ```
7. Print the result
   ```python
   print(top_6_likelihood)
   ```

Combining all the steps, the final code looks like this:
