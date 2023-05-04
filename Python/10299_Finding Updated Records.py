# Question ID:- 10299
# Question name :- Finding Updated Records

import pandas as pd
result = pd.DataFrame( columns=['id' , 'first_name' , 'last_name', 'department_id', 'salary'])
for ID, d in ms_employee_salary.groupby( 'id' ):
    # we are taking only max salary row because of salary increases every year 
    temp= d[d.salary==d.salary.max()] [['id' , 'first_name' , 'last_name', 'department_id', 'salary'] ]
    result= result.append( temp )
result.head( result.shape[0] )
