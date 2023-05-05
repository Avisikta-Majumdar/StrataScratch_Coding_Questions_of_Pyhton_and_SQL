select emp.location, avg(ser.popularity) as avg_popularity 
from facebook_employees as emp inner join facebook_hack_survey ser
on emp.id=ser.employee_id
group by emp.location;