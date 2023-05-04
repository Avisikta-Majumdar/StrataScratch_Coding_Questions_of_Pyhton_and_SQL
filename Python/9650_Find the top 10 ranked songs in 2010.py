import pandas as pd
df = billboard_top_100_year_end[ billboard_top_100_year_end.year==2010][
    ['year_rank', 'group_name', 'song_name']].sort_values( 'year_rank')
df.drop_duplicates( subset = 'year_rank', inplace=True )
df.head(10 )
