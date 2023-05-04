import pandas as pd
df = customers.merge(orders, left_on='id', right_on='cust_id')
df = df[ (df.first_name=='Jill') | (df.first_name=='Eva') ]
df[['first_name', 'order_date', 'order_details', 'total_order_cost']].head( df.shape[0])
