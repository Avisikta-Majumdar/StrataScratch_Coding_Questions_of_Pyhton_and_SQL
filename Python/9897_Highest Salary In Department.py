import pandas as pd
df = employee.copy()
res = [ [dept, d_df[ d_df.salary==d_df.salary.max()]['first_name'].values[0] ,
    d_df[ d_df.salary==d_df.salary.max()]['salary'].values[0]] for dept, d_df in df.groupby( 'department' ) ]
res.sort(reverse=True, key = lambda x: x[-1])
result = pd.DataFrame( res, columns=[ 'department', 'first_name', 'salary' ])
result.head()