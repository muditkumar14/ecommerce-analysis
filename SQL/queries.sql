-- E-commerce SQL Queries
-- We will add queries here step by step
select count(*) 
from orders;

select count(customer_id) 
from customers;

select sum(amount)
from orders;

select customer_id, sum(amount) as total_spent
from orders
group by customer_id;

select customer_id, sum(amount) as total_spent
from orders
group by customer_id
order by total_spent desc
limit 1;

Select City, sum(amount) as total_revenue
from Customers
join Orders
on Customers.customer_id = Orders.customer_id
group by city
order by sum(amount) desc;

select strftime('%Y-%m', order_date) as month, sum(amount) as total_revenue
from orders
group by month
order by total_revenue desc;

