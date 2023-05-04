import pandas as pd
df = facebook_employees.merge( facebook_hack_survey, left_on='id', right_on='employee_id')
res = [ [ cntry, ( c_df.popularity.sum() / c_df.shape[0] )] for cntry, c_df in df.groupby('location' )]
result = pd.DataFrame(  res ,columns= [ 'location', 'popularity' ])
result.head()
