import pandas as pd
import warnings
warnings.filterwarnings('ignore')
# Load the dataset
df = pd.read_parquet('data/050_ING.parquet')
# Filter out the columns 'lang' and 'favorites' from the dataframe
df = df[['lang', 'favorites']]
# Find the language with the highest number of favorites
most_favorited_language = df.groupby('lang')['favorites'].sum().idxmax()
# Print the result
print(most_favorited_language)