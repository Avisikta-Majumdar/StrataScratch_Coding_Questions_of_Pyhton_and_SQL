import pandas as pd
r= spotify_worldwide_daily_song_ranking.groupby('artist')
res=[]
for a, a_df in r:
    res.append( [a, a_df.shape[0]])
r = pd.DataFrame(res, columns=['artist', 'n_occurences'])
r.sort_values('n_occurences', ascending=False, inplace=True)
r
