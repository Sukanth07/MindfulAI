use farmers_set;


-- 1.  Extract the top 15 rows and customer_id and customer_first_name
SELECT customer_id, customer_first_name FROM customer LIMIT 15;

-- 2. Extract the top 15 rows with the same columns and skip the first 2 rows
SELECT customer_id, customer_first_name FROM customer LIMIT 15 OFFSET 2;

-- 3. Sort the customer table by customer_names
SELECT * FROM customer ORDER BY customer_first_name;

-- 4. Sort the customers table by descending order with respect to customer_id
SELECT * FROM customer ORDER BY customer_id DESC;

-- 5. Extract all the data whose customer_zip is 22801
SELECT * FROM customer WHERE customer_zip=22801;

-- 6. Extract all data whose zip code is other than 22801
SELECT * FROM customer WHERE customer_zip<>22801;

-- 7. Sort all the data whose customer id's is greater than 10 as well as the pincode in 22801
SELECT * FROM customer WHERE customer_id>10 and customer_zip=22801;

-- 8. What would be the total number of customer_id
SELECT COUNT(DISTINCT customer_id) FROM customer;

-- 9. Sort out the data till the date 5th May 2019 only with the columns market_date and market_start_datetime from the market_date_info table
SELECT market_date, market_start_time FROM market_date_info WHERE market_date<='2019-05-05' ORDER BY market_date;

-- 10. Extract all the products whose product size is medium and large
SELECT * FROM product WHERE product_size='medium' or product_size='large';