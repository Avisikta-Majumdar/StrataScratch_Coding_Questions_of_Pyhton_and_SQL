import pandas as pd
import numpy as np
grp = employee.groupby("department")
avg_sal= {}
for dept, ddf in grp:
    avg_sal[dept] = np.mean(ddf.salary)
avg_Sal = [avg_sal[d] for d in employee.department.values]
employee['avg_salary'] = avg_Sal
employee[['department', 'first_name', 'salary', 'avg_salary']].head( employee.shape[0])
