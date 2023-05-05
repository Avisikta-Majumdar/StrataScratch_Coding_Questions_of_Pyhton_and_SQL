 select (select max(salary)  from db_dept as dept 
inner join db_employee emp on emp.department_id=dept.id 
where dept.department='marketing') - 
(select max(salary)  from db_dept as dept 
inner join db_employee emp on emp.department_id=dept.id 
where dept.department='engineering') as salary_difference;