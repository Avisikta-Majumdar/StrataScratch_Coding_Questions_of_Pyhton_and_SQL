import pandas as pd
df = ms_user_dimension.merge( ms_acc_dimension, on='acc_id')
df = df.merge( ms_download_facts, on='user_id' )
data =[ [ date_, d_df[ d_df.paying_customer=='no'].downloads.sum() , d_df[ d_df.paying_customer=='yes'].downloads.sum() ]  for date_ , d_df in df.groupby( 'date' ) ]
result = pd.DataFrame( data, columns=['date', 'no', 'yes'] )
result = result[ result.no>result.yes]
result.head( result.shape[0] )