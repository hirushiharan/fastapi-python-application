CREATE DATABASE IF NOT EXISTS outlet;
USE outlet;

-- Create the user table
CREATE TABLE IF NOT EXISTS user (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50),
    email VARCHAR(255),
    password VARCHAR(255)
);

-- Create the customer table
CREATE TABLE IF NOT EXISTS customer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    image LONGTEXT,
    nic LONGTEXT
);

-- Create the address table
CREATE TABLE IF NOT EXISTS address (
    address_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    line1 VARCHAR(255),
    line2 VARCHAR(255),
    city VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
);

-- Create the contact table
CREATE TABLE IF NOT EXISTS contact (
    contact_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    mobile_no INT,
    email VARCHAR(100),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
);

-- Create the request table
CREATE TABLE IF NOT EXISTS request (
    request_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    request_type VARCHAR(50),
    market VARCHAR(50),
    channel VARCHAR(50),
    brand VARCHAR(50),
    is_outlet BOOLEAN,
    is_chain_outlet BOOLEAN,
    chain_name VARCHAR(100),
    status VARCHAR(50),
    requested_by VARCHAR(50),
    requested_on DATE,
    assigned_to VARCHAR(50),
    assigned_on DATE,
    reviewed_by VARCHAR(50),
    reviewed_on DATE,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
);
