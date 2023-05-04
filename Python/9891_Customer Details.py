import pandas as pd
df = customers.merge(orders,left_on='id', right_on='cust_id', how='left')
df.drop_duplicates(inplace=True)
res = df[[ 'first_name', 'last_name', 'city', 'order_details' ]]
res.sort_values(by=['first_name', 'order_details'], inplace=True)
res.head( res.shape[0] )
