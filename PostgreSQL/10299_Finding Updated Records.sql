select distinct id, first_name, last_name, department_id, max(salary)
over(PARTITION BY id) as max 
from ms_employee_salary
order by id;