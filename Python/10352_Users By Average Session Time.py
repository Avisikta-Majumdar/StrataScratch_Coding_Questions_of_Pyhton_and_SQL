import pandas as pd
from datetime import datetime as dt

def calculate_seconds( s ):
    h,m,s=[ int(i) for i in s.split(':')]
    return ( (60*60*h) + (m*60) + s)
    
df = facebook_web_log.copy()
df = df[ (df.action!='scroll_up')]
df = df[ (df.action!='scroll_down' )]
df['Date'] = [str(i)[:10] for i in df.timestamp]
df.head()
data=[]
for user_ID , user_grp in df.groupby( ['user_id', 'Date'] ):
    if len( user_grp[ user_grp.action=='page_exit' ].index ):
        spend = str( (user_grp[ user_grp.action=='page_exit'].timestamp.min()) - ( user_grp[ user_grp.action=='page_load'].timestamp.max()) )[-8:]
        total_seconds = calculate_seconds( spend )
        data.append( [user_ID[0] , total_seconds])
data = pd.DataFrame( data, columns=[ 'user_id', 'duration'] )        

result = [ [id, d_df.duration.mean()] for id, d_df in data.groupby( 'user_id' ) ] 
result = pd.DataFrame( result, columns=['user_id', 'duration'])
result.head()