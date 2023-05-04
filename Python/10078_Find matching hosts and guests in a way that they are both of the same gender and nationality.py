import pandas as pd
df = airbnb_hosts.merge( airbnb_guests , left_on =['nationality', 'gender'], right_on =['nationality', 'gender'] , suffixes =('', '_y' )).drop_duplicates( subset=['nationality', 'gender'])[[ 'host_id', 'guest_id' ]]
df.head( df.shape[0] )
