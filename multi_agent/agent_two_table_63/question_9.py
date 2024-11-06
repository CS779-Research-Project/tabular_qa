import pandas as pd

df = pd.read_parquet('data/063_Influencers.parquet')
df = df[['name', 'page_rank_norm']]
highest_page_rank_norm = df['page_rank_norm'].max()
entity = df[df['page_rank_norm'] == highest_page_rank_norm]['name']
print(entity)