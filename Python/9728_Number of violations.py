import pandas as pd
df = sf_restaurant_health_violations[sf_restaurant_health_violations.business_name=='Roxanne Cafe']
df['year'] = pd.to_datetime( df['inspection_date'] ).dt.year
result =[ [ yr, df_.shape[0] ] for yr, df_ in df.groupby( 'year' ) ]
result = pd.DataFrame( data=result , columns=['inspection_date' , 'violation_id']).sort_values( 'inspection_date')
result.head( result.shape[0] )
