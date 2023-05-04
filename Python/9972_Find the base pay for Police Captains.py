import pandas as pd
df = sf_public_salaries[ sf_public_salaries.jobtitle=='CAPTAIN III (POLICE DEPARTMENT)' ][ ['employeename', 'basepay' ]  ]
df.head( df.shape[0] )
