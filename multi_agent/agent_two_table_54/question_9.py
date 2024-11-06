import pandas as pd
import warnings
warnings.filterwarnings('ignore')
# Load the dataset
df = pd.read_parquet('data/054_Joe.parquet')
# Filter out the columns 'author_name' and 'user_favourites_count' from the dataframe
df = df[['author_name<gx:category>', 'user_favourites_count<gx:number>']]
# Group the dataframe by 'author_name'
grouped = df.groupby('author_name<gx:category>')
# Find the author with the highest 'user_favourites_count'
highest_favourites = grouped['user_favourites_count<gx:number>'].max()
# Print the author's name
print(highest_favourites.idxmax())