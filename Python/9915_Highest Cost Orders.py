import pandas as pd
df = customers.merge( orders, left_on='id', right_on='cust_id' )
o_date = df.order_date.unique()
df = df[ (df.order_date>='2019-02-01') & (df.order_date<='2019-05-01') ][['first_name', 'total_order_cost', 'order_date' ]]
result = []
for name, n_df in df.groupby([ 'first_name', 'order_date' ]):
    result.append( [ name[0], name[1], n_df.total_order_cost.sum()] )
result = pd.DataFrame( result, columns = ['first_name', 'order_date', 'max_cost' ])
result = result[ result.max_cost==result.max_cost.max()]
result.head()