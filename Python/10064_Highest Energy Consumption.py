# Import your libraries
import pandas as pd
df = pd.concat( [  fb_eu_energy, fb_asia_energy, fb_na_energy ], ignore_index=True)
data = [ [d, d_df.consumption.sum()] for d, d_df in df.groupby( 'date' ) ]
data.sort( reverse=True, key = lambda x:x[1]) # sorting the values by consumption value in decreasing order
result = pd.DataFrame( data, columns=['date', 'consumption'])
result[ result.consumption==result.consumption.max() ].head() 