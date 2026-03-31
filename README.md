# Introduction to Databases

SQL practice exercises and database fundamentals covering MySQL database creation, table operations, and Python-MySQL connectivity.

## Overview

This repository contains hands-on SQL exercises and scripts demonstrating core database concepts including:

- Database and table creation
- Data insertion and queries
- SQL constraints and relationships
- Python-MySQL integration

## Contents

### SQL Scripts

- **`alx_book_store.sql`** — Complete bookstore database schema
- **`task_2.sql`** — Table creation exercises
- **`task_3.sql`** — Data insertion queries
- **`task_4.sql`** — SELECT queries and filtering
- **`task_5.sql`** — UPDATE operations
- **`task_6.sql`** — Advanced queries (JOINs, aggregations)

### Python Integration

- **`MySQLServer.py`** — Python script for MySQL database connection and operations

## Quick Start

### Prerequisites

- MySQL Server 5.7+ or MariaDB 10.3+
- Python 3.6+ (for Python scripts)
- `mysql-connector-python` package

### Installation

```bash
# Clone repository
git clone https://github.com/FredrickMbithi/Intro_to_DB.git
cd Intro_to_DB

# Install Python MySQL connector (if using Python scripts)
pip install mysql-connector-python
```

### Running SQL Scripts

```bash
# Connect to MySQL
mysql -u root -p

# Create database
mysql> CREATE DATABASE alx_book_store;
mysql> USE alx_book_store;

# Execute schema
mysql> SOURCE alx_book_store.sql;

# Run individual tasks
mysql> SOURCE task_2.sql;
mysql> SOURCE task_3.sql;
# ... etc
```

### Running Python Script

```python
# Edit MySQLServer.py with your credentials
python MySQLServer.py
```

## Database Schema (alx_book_store)

### Tables

**Books Table:**
- `book_id` (Primary Key)
- `title`
- `author`
- `price`
- `quantity`

**Customers Table:**
- `customer_id` (Primary Key)
- `name`
- `email`
- `address`

**Orders Table:**
- `order_id` (Primary Key)
- `customer_id` (Foreign Key)
- `order_date`
- `total_amount`

## Exercise Tasks

### Task 2: Table Creation
Creating tables with proper constraints:
```sql
CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(130),
    author VARCHAR(130),
    price DOUBLE,
    quantity INT
);
```

### Task 3: Data Insertion
Inserting sample records:
```sql
INSERT INTO books (title, author, price, quantity)
VALUES ('Harry Potter', 'J.K. Rowling', 29.99, 50);
```

### Task 4: SELECT Queries
Retrieving and filtering data:
```sql
SELECT * FROM books WHERE price > 20;
SELECT title, author FROM books WHERE author LIKE '%Rowling%';
```

### Task 5: UPDATE Operations
Modifying existing records:
```sql
UPDATE books SET price = 24.99 WHERE book_id = 1;
UPDATE books SET quantity = quantity - 1 WHERE title = 'Harry Potter';
```

### Task 6: Advanced Queries
JOINs, aggregations, and complex queries:
```sql
SELECT customers.name, COUNT(orders.order_id) as total_orders
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id;
```

## 🐍 Python-MySQL Integration

### Example: Connecting to Database

```python
import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='alx_book_store'
)

cursor = conn.cursor()

# Execute query
cursor.execute("SELECT * FROM books")
results = cursor.fetchall()

for row in results:
    print(row)

# Close connection
cursor.close()
conn.close()
```

### MySQLServer.py Features

The included Python script demonstrates:
- Database connection management
- Executing SQL queries from Python
- Fetching and processing results
- Error handling for database operations

## Learning Objectives

By completing these exercises, you will understand:

1. **Database Design**
   - Creating databases and tables
   - Defining primary keys and foreign keys
   - Setting constraints (NOT NULL, UNIQUE, etc.)

2. **SQL Operations**
   - INSERT, SELECT, UPDATE, DELETE
   - WHERE clauses and filtering
   - JOINs (INNER, LEFT, RIGHT)
   - Aggregation functions (COUNT, SUM, AVG)
   - GROUP BY and HAVING

3. **Python Integration**
   - Connecting Python to MySQL
   - Executing queries programmatically
   - Processing query results
   - Transaction management

## Common SQL Commands

```sql
-- Show all databases
SHOW DATABASES;

-- Select database
USE alx_book_store;

-- Show tables
SHOW TABLES;

-- Describe table structure
DESCRIBE books;

-- Show table creation SQL
SHOW CREATE TABLE books;
```

## Resources

**MySQL Documentation:**
- [Official MySQL Docs](https://dev.mysql.com/doc/)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)

**Python MySQL:**
- [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/)

## ⚠️ Security Notes

**For Production:**
- Never hardcode database credentials
- Use environment variables or config files (not committed to git)
- Implement proper user authentication
- Use prepared statements to prevent SQL injection
- Limit database user permissions (principle of least privilege)

**Example with environment variables:**

```python
import os
import mysql.connector

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)
```

## Testing Your Queries

Before running queries on production data:

1. Backup your database
2. Test queries on sample data first
3. Use TRANSACTIONS for multi-step operations
4. Verify results with SELECT before UPDATE/DELETE

```sql
-- Start transaction
START TRANSACTION;

-- Run your UPDATE/DELETE queries
UPDATE books SET price = price * 1.1;

-- Check results
SELECT * FROM books;

-- If satisfied, commit; otherwise rollback
COMMIT;
-- or
ROLLBACK;
```

## Best Practices

1. **Naming Conventions**
   - Use lowercase with underscores: `customer_id`, `order_date`
   - Table names should be plural: `books`, `customers`
   - Be consistent across your schema

2. **Indexing**
   - Add indexes to frequently queried columns
   - Primary keys are automatically indexed
   - Foreign keys should be indexed

3. **Data Types**
   - Use appropriate data types (INT for IDs, VARCHAR for text, DECIMAL for money)
   - Specify length constraints where appropriate
   - Use DATETIME for timestamps, not strings

## License

Educational project - MIT License

## Author

Fredrick Mbithi

---

**Course:** Introduction to Databases  
**Database:** MySQL / MariaDB  
**Focus:** SQL Fundamentals & Python Integration  
**Status:** Educational Exercises
