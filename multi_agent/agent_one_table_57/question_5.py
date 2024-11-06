   import pandas as pd
   ```

2. Load the dataset '057_Spain.parquet' into a pandas DataFrame.
   ```python
   df = pd.read_parquet('data/057_Spain.parquet')
   ```

3. Filter out the 'Age' column from the DataFrame to work only with the relevant data.
   ```python
   age = df['Age']
   ```

4. Calculate the average age using the mean function on the 'Age' column.
   ```python
   average_age = age.mean()
   ```

5. Print the result to display the average age of the respondents.
   ```python
   print(average_age)
   ```

Putting it all together, the complete Python code to find the average age of the respondents in the '057_Spain' dataset is:
