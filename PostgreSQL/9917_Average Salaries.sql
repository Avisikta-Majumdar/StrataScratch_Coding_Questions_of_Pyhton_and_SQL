select department, first_name, salary, avg(salary) 
over(PARTITION BY department)
from employee;