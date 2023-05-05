 select date_part('year',inspection_date) as year, count(*) from sf_restaurant_health_violations
where business_name like 'Roxanne Cafe'
group by 1
order by 1;