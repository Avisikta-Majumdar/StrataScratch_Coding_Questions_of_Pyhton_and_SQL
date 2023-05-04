import pandas as pd
df = db_employee.merge( db_dept, left_on='department_id', right_on ='id' )
df_marketing_max_sal = df[ df.department=='marketing'].salary.max()
df_eng_max_sal = df[ df.department=='engineering' ].salary.max()
result = pd.DataFrame( data=[(df_marketing_max_sal- df_eng_max_sal)], columns=['salary_difference'])
result.head()
