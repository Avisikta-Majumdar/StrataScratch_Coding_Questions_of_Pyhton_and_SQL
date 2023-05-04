import pandas as pd
airbnb_hosts = airbnb_hosts[ airbnb_hosts.age<31]
airbnb_units = airbnb_units[ airbnb_units.unit_type=='Apartment']
df = airbnb_hosts.merge( airbnb_units, on='host_id' )
val=[]
for nation, ddf in df.groupby( 'nationality'):
    val.append( [nation , ddf.city.nunique() ] )
result = pd.DataFrame( val, columns=['nationality', 'apartment_count']).sort_values( 'apartment_count', ascending=False )
result.head( 1 )
