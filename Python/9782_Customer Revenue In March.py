import pandas as pd
df = orders[ (orders.order_date.dt.year==2019) & (orders.order_date.dt.month==3) ]
df[ df.cust_id==3][['cust_id', 'total_order_cost']]
data = [ [c_id, c_id_df.total_order_cost.sum()] for c_id, c_id_df in df.groupby( 'cust_id')]
data.sort( reverse=True, key = lambda x: x[1])
df = pd.DataFrame( data, columns=['cust_id', 'revenue'])
df