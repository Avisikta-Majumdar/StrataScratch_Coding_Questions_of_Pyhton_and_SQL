import pandas as pd
result = [ [ g_id, g_id_df.n_messages.sum() ] for g_id, g_id_df in airbnb_contacts.groupby( 'id_guest' )]
sums = set( [i[-1] for i in result] )
sums= list( sums )
sums.sort( reverse=True )
sums.insert(0, 123456789)
result.sort(reverse=True, key = lambda x: x[1])
result = pd.DataFrame( data= result, columns=[['id_guest', 'n_messages']])
result[ 'ranking' ] = [sums.index( i ) for i in result.n_messages.values]
result = result[['ranking', 'id_guest', 'n_messages']]
result.head( result.shape[0] )