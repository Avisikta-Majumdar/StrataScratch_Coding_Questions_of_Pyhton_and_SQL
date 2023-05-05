select c.first_name, sum(o.total_order_cost) total_order_cost, o.order_date 
from customers c join orders o
on c.id=o.cust_id
where order_date>='2019-02-01' and order_date<='2019-05-01'
group by c.first_name, o.order_date
order by 2 desc
limit 1