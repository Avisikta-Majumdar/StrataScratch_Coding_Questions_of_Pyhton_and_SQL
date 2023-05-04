import pandas as pd
vals = forbes_global_2010_2014.profits.unique()
vals.sort()
vals= vals[ -3: ]
result = forbes_global_2010_2014[ forbes_global_2010_2014.profits.isin( vals ) ][[ 'company', 'profits']]
result.sort_values( by='profits', ascending=False, inplace=True)
result.head( )
