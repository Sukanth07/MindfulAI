use mfai;

create table nri_info(
	nri_id int primary key not null,
    nri_name varchar(30),
    age int,
    dob varchar(10) unique,
    phoneno varchar(10),
    msalary_inr int check (msalary_inr>20000),
    tax_in_inr int,
    resi_city varchar(20),
    work_country varchar(20),
    birth_country varchar(20) default 'India');
    
    
use farmers_set;

select * from customer_purchases;

select extract(hour from transaction_time) as transaction_hour, vendor_id, customer_id, product_id, cost_to_customer_per_qty from customer_purchases;

select customer_id, vendor_id, min(quantity*cost_to_customer_per_qty) as min_total  from customer_purchases group by customer_id, vendor_id;