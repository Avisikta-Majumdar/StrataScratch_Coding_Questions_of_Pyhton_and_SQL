import pandas as pd
df = yelp_business.copy()
df = df[ df.stars==5 ]
business_count_by_state_grp = [ [stat, s_df.shape[0], ] for stat, s_df in df.groupby( 'state' )] 
business_count_by_state_grp.sort( reverse=True, key = lambda x: x[1])
res = pd.DataFrame( business_count_by_state_grp , columns=[ 'state', 'n_business'] )
res.head( 6 )