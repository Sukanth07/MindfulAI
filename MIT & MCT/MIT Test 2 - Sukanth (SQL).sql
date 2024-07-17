-- MIT - 2 SQL (23-30-2024 SATURDAY)

-- ANSWER ALL OF THE FOLLOWING QUESTION :
-- AFTER THE END OF EVERY CODE PLEASE DO COMMENT ON YOUR QUERY

-- -----------------------
use farmers_set;
-- -----------------------

-- 01. CREATE A TABLE NAMED LIBRARY WHITH 5 RECORDS AND ATTRIBUTES ONLY WITH THE SPECIFIED DATA TYPE  ALONG WITH THIER CONSTRAINTS.

-- BOOK_ID INT
-- BOOK_NAME VARCHAR
-- AUTHOR_NAME VARCHAR
-- DATE_OF_PUBLISH DATE
-- PRICE INT

create table library(
	book_id int,
    book_name varchar(20),
    author_name varchar(20),
    date_of_publish date check (date_of_publish<='2020-01-10'),
    price int default 350);

alter table library
add genre varchar(20);

insert into library 
(book_id, book_name, author_name, date_of_publish, price, genre)
values
(1, 'Ramayana', 'Kambar', '2019-02-28', 500, 'history'),
(2, 'Loki', 'Marvel', '2018-12-28', 700, 'comic'),
(3, 'Thirukural', 'Thiruvalluvar', '2000-02-03', 200, 'history'),
(4, 'Mahabaratam', 'Modi', '1940-12-01', 500, 'history'),
(5, 'Infinity War', 'Marvel', '2002-02-28', 900, 'comic');

update library
set author_name='Tagore' where author_name='Kambar';

-- a. THE DATE OF PUBLISH SHOULD NOT BE AFTER 2020-01-10.
-- b. THE PRICE SHOULD BE KEPT IN 350 IF NO VALUES ARE ENTRED.
-- c. ADD A NEW COLUMN CALLED GENRE WITH ITS DATA TYPE.
-- d. UPDATE YOUR AUTHOR NAME FROM EXISITING TO TAGORE.

-- -------------------------- END OF 01  -------------------------------------------------------------

-- 02. WRITE A QUERY TO FIND THE DISTINCT COUNT OF THE VENDOR_ID IN THE VENDOR_INVENTORY TABLE.

select count(distinct vendor_id) 
from vendor_inventory;

-- --------------------------- END OF 02 --------------------------------------------------------------


-- 03. FIND THE TOTAL_PRICE OF THE VENDOR_INVENTORY TABLE AND SHOW THE HIGHEST 20 RESULTS.

select 
max(quantity*original_price) as max_total 
from vendor_inventory;

-- ---------------------------- END OF 03 --------------------------------------------------------------


-- 04. FILTER OUT ALL THE RECORDS WHOSE VENDOR_OWNER_FIRST_NAME THAT HAS 'A' AT THE SECOND POSITION

select * 
from vendor 
where vendor_owner_first_name like '_A%';

-- ---------------------------- END OF 4 ----------------------------------------------------------------

-- 05. WHAT IS THE AVERAGE TOTAL_AMT SPENT PER PURCHASE BY EACH CUSTOMER,VENDOR,QUANTITY, COST_CUSTOMER_PER_QTY COMBINATION,WHERE THE AVERAGE TOTAL_AMT EXCEEDS 20 
--     PROVIDE THE CUSTOMER_ID, VENDOR_ID, QUANTITY, COST_CUSTOMER_PER_QTY FOR EACH RECORD.

select * from customer_purchases;

select 
customer_id, avg(quantity*cost_to_customer_per_qty) as total_amt 
from customer_purchases 
group by customer_id;

select 
vendor_id, avg(quantity*cost_to_customer_per_qty) as total_amt 
from customer_purchases 
group by vendor_id;

select 
quantity, avg(quantity*cost_to_customer_per_qty) as total_amt 
from customer_purchases 
group by quantity;

select 
cost_to_customer_per_qty, avg(quantity*cost_to_customer_per_qty) as total_amt 
from customer_purchases 
group by cost_to_customer_per_qty;

-- ----------------------------------------