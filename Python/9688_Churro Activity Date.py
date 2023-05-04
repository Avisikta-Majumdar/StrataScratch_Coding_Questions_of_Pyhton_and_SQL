import pandas as pd
df = los_angeles_restaurant_health_inspections[ (los_angeles_restaurant_health_inspections.facility_name=='STREET CHURROS') &
                                                ( los_angeles_restaurant_health_inspections.score<95) ]
df[[ 'activity_date', 'pe_description']].head( df.shape[0] )
