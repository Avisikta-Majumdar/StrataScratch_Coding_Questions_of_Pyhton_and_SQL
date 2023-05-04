import pandas as pd
df = forbes_global_2010_2014 [ forbes_global_2010_2014.sector =='Financials' ] [
        [ 'company','continent', 'profits'] ].sort_values( by='profits', ascending=False)
df[['company', 'continent']].head(1)
