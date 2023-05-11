import pandas as pd
df = google_file_store.copy()
temp= " ".join( list( df.contents.values ))
bull , bear= temp.count( 'bull' ),  temp.count( 'bear' )
result = pd.DataFrame( [['bull', bull], ['bear', bear]], columns=[ 'word','netry' ])
result.head()