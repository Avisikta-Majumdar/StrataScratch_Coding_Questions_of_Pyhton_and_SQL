import pandas as pd
df = olympics_athletes_events[ ['games', 'id']]
result = pd.DataFrame( [ [ mm_yy , ddf.id.nunique() ] for mm_yy , ddf in df.groupby( 'games' ) ] 
                      , columns =['games', 'athletes_count' ]).sort_values( by ='athletes_count', ascending=False)
result.head(1)
