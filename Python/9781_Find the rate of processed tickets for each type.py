import pandas as pd
type_grp = facebook_complaints.groupby('type')
r=[]
for Type, type_df in type_grp:
    total = type_df.shape[0]
    true_count = sum([1 if i==True else 0 for i in type_df.processed.values])
    rate = round( (true_count/total) ,3)
    r.append([Type, rate])
print( r )
result= pd.DataFrame(r , columns=['type', 'processed_rate'])
result.head()
