-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;

-- Use the created database
USE hbtn_0e_6_usa;

-- Create 'states' table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

-- Insert sample data
INSERT INTO states (name) VALUES
    ('California'),
    ('New York'),
    ('Texas'),
    ('Florida');
