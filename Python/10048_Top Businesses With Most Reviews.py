import pandas as pd
val=[]
for na , df in yelp_business.groupby( 'name' ):
    val.append( [na, df.review_count.sum() ])
res= pd.DataFrame( val, columns=["name", 'review_count' ] )
res.sort_values( 'review_count',ascending=False, inplace=True )
res.head()
