import pandas as pd
# using groupby on worker_ref_id for calculating total bonus amount for each worker
sf_bonus_ = [[id, d_df.bonus.sum()] for id, d_df in sf_bonus.groupby( 'worker_ref_id' )]
sf_bonus = pd.DataFrame( sf_bonus_, columns=[ 'worker_ref_id', 'bonus'] )
df = sf_employee.merge( sf_bonus, left_on='id' , right_on='worker_ref_id'  )
df['avg_total_comp'] = df.salary + df.bonus
df= df[['employee_title', 'sex', 'avg_total_comp']]
df.sort_values(by=[ 'employee_title', 'sex' ], inplace=True)
result = []
for title, d_df in df.groupby( 'employee_title' ):
    result.append( [ title, d_df.sex.unique()[0], int (d_df.avg_total_comp.mean()) ]  )
df = pd.DataFrame( result, columns=['employee_title', 'sex', 'avg_total_comp'] )
df.head( df.shape[0] )