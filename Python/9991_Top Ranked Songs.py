import pandas as pd
top_song= spotify_worldwide_daily_song_ranking[ spotify_worldwide_daily_song_ranking.position==1]
top_song_grp= top_song.groupby( 'trackname' )
res = pd.DataFrame( [[tname, len(df)] for tname, df in top_song_grp ], columns=['trackname', 'times_top1'] ).sort_values( 'times_top1' , ascending=False)
res
