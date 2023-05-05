select host.nationality, count(distinct unit_type) as apartment_count 
from airbnb_units units join airbnb_hosts as host
on host.host_id=units.host_id
where host.age<30
group by host.nationality
order by 2 desc
limit 1 offset 1;