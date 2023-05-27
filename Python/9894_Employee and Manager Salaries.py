import pandas as pd
df = employee.copy()
df= df[['id', 'first_name', 'salary', 'manager_id']]
result = df.merge( df,  left_on='manager_id', right_on='id' )
result = result[ result.salary_x> result.salary_y][ [ 'first_name_x', 'salary_x' ] ]
result.head()