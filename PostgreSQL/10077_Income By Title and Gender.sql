select employee_title, sex, avg(avg_compensation) from 
( select sf_employee.employee_title as employee_title , sf_employee.sex, ( sf_employee.salary + sf_bonus.sum) as avg_compensation
     from sf_employee inner join 
            (select worker_ref_id, sum(bonus) from sf_bonus group by worker_ref_id ) as sf_bonus 
            -- created a new table bonus which contains total bonus for each empolyees
    on sf_employee.id = sf_bonus.worker_ref_id)  as df -- merging sf_employee & df_bonus and gave a new name called df
group by employee_title, sex ; -- using groupby function on employee_title & sex column