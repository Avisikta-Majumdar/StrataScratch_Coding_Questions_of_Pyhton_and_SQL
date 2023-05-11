import pandas as pd
from itertools import combinations
from datetime import datetime as dt
df= amazon_transactions.copy()
result_ids = []
for u_id, u_df in df.groupby( 'user_id' ):
    if u_df.shape[0]>1:
        unique_dates = u_df.created_at.values
        unique_dates_combination = list(combinations(unique_dates, 2))
        temp=[]
        for every_combo in unique_dates_combination:
            delta = ( (dt.strptime( str(every_combo[-1])[ :10 ] , "%Y-%m-%d")) -  ( dt.strptime(str(every_combo[0])[:10], "%Y-%m-%d") )).days
            temp.append( delta)
        temp = [abs(i) if i<0 else i for i in temp]
        if min(temp)<8:
            result_ids.append( u_id )
result = pd.DataFrame(data= result_ids, columns=['0'] )
result.head( result.shape[0])