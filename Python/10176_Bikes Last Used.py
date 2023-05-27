import pandas as pd
df = dc_bikeshare_q1_2012.copy()
data = [[b_no, max(d_df.end_time.unique())] for b_no,d_df in df.groupby( 'bike_number' )]
result = pd.DataFrame( data, columns=['bike_number', 'last_used'])
result.sort_values( by='last_used', ascending=False, inplace=True)
result.head( result.shape[0] )