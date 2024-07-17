-- /*
-- 1. Basic SQL Syntax (10 points): (5 marks)

-- Write a SQL SELECT statement to retrieve all columns from a table named "customers". 
-- How can you filter rows in a SELECT statement using a WHERE clause? Provide an example. 
-- Write a SQL statement to sort the results of a SELECT query by a specific column in descending order. 
-- What operator can be used to combine multiple conditions in a WHERE clause? 
-- Give an example of an alias used for a table name in a SELECT statement. 


-- 2-This scenario involves creating a database for a library management system, populating it with data, and performing various operations using SQL queries.(10 marks)

-- 1. Database and Table Creation:

-- Write SQL statements to achieve the following:

-- Create a database named library.
-- Inside the library database, create a table named books with the following columns:
-- book_id (INTEGER, PRIMARY KEY)
-- title (VARCHAR(255))
-- author (VARCHAR(255))
-- genre (VARCHAR(50))
-- year_published (INTEGER)

-- 2. Data Insertion:

-- Prepare and execute SQL statements to insert sample book data into the books table. You can include at least 5 different books with varying titles, authors, genres, and publication years.

-- 3. Data Retrieval and Manipulation:

-- Write SQL queries to perform the following operations:

-- Retrieve all book titles and publication years from the books table.
-- Find all books published after a specific year (e.g., 2010).
-- Find books written by a particular author (e.g., "J.R.R. Tolkien").
-- Filter and display books belonging to a specific genre (e.g., "Science Fiction").
-- Update the genre of a book (e.g., change "Mystery" to "Thriller" for a specific book_id).
-- Delete a book from the table based on its book_id .
-- . /*

use farmers_set;

-- 1.i)
SELECT *
FROM customer;

-- 1.ii) 
-- We can use WHERE clause followed by a condition
SELECT *
FROM customer
WHERE customer_id <= 5;

-- 1.iii)
SELECT *
FROM customer
ORDER BY customer_id DESC;

-- 1.iv)
-- We can use logical operators like 'and', 'or' to combine multiple conditions
SELECT *
FROM customer
WHERE customer_id > 5 and customer_zip = 22801;

-- 1. v)
SELECT concat(customer_first_name, customer_last_name)
AS customer_full_name
FROM customer;

-- --------------------------------------------------------------------------------------------------------

-- 2.1)
create database library;
use library;
create table books(
	book_id int primary key,
    title varchar(255),
    author varchar(255),
    genre varchar(50),
    year_published int);
    
-- 2.2)
insert into books
(book_id, title, author, genre, year_published)
values
(1, 'Secret Invasion', 'Nick Fury', 'Comic', 2023),
(2, 'Mahabaratham', 'Edison', 'History', 2000),
(3, 'Leo', 'Loki', 'Violence', '2023'),
(4, 'Vikram', 'Kamal Hasan', 'Romance', 2022),
(5, 'Jailer', 'Nelson', 'Comedy', 2024);


-- 2.3.i)
SELECT title, year_published
FROM books;

-- 2.3.ii)
SELECT title as books_after_2010
FROM books
WHERE year_published > 2010;

-- 2.3.iii)
SELECT *
FROM books
WHERE author = 'Loki';

-- 2.3.iv)
SELECT *
FROM books
WHERE genre = 'comic';

-- 2.3.v)
UPDATE books
SET genre = 'Thriller'
WHERE book_id = 5;

-- 2.3.vi)
DELETE 
FROM books 
WHERE book_id = 3;


