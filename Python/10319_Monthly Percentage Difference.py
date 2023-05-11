import numpy as np 
import pandas as pd
def SpliT( x ):
    x = str(x)
    return x[:7]

df = sf_transactions.copy()
df['month' ]= df.created_at.dt.month
df.month = df.month.astype( int )
df[ 'created_at' ] = df.created_at.astype( str ).apply( SpliT )
df.rename( columns = {'created_at':'year_month'}, inplace = True)
df = df[['month', 'year_month' , 'value']]

df.sort_values( by='month', inplace=True)
data = [ [ y_m , y_m_df.value.sum(), y_m_df.month.unique()[0]] for y_m , y_m_df in df.groupby( 'year_month' )]
data.sort( key = lambda x: x[-1] )

result = pd.DataFrame( data , columns=['year_month', 'total_revenue_of_the_month', 'month'])
result.month = result.month.astype( int )

pft_loss = [ np.nan ]
for mo in range( 2,13 ):
    prev_mo_revnue = result[ result.month==(mo-1) ].total_revenue_of_the_month.unique()[0]
    this_mo_revnue = result[ result.month==mo ].total_revenue_of_the_month.unique()[0]
    p_l = ( (( this_mo_revnue-prev_mo_revnue )/prev_mo_revnue)*100)
    p_l = round( p_l , 2 )
    pft_loss.append( p_l )
        
result['revenue_diff_pct'] = pft_loss
result[[ 'year_month','revenue_diff_pct' ]].head( 12 )