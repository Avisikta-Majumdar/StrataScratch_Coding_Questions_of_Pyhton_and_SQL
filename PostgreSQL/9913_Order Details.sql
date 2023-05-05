select first_name, order_date, order_details,total_order_cost from customers as c inner join orders as o on c.id=o.cust_id
where first_name in ('Jill', 'Eva')
order by first_name desc;