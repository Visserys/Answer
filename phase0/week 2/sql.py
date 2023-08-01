CREATE TABLE Customer (
	id primary KEY,
	customer_id int,
	customer_name varchar(50) NOT null,
	city varchar(50) NOT null

);

CREATE TABLE Orders (
	order_id int primary key ,
	customer_id int, 
	order_date date,
	total_amount float

);

insert into Customer (customer_id ,customer_name ,city)
values 
	(1,'John Doe','New York'),
	(2,'Jane Smith','Los Angels'),
	(3,'David Johnson','Chicago');

insert into Orders (order_id, customer_id ,order_date ,total_amount)
values 
	(1,1,'2022-01-10',100),
	(2,1,'2022-02-15',150),
	(3,2,'2022-03-20',200),
	(4,3,'2022-04-25',50);

SELECT Customer.customer_name, count(Orders.customer_id) as Total_orders
FROM Customer
JOIN Orders ON customer.customer_id= Orders.customer_id
group by Customer.customer_name;


select * from Customer;
select * from Orders;




