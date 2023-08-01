--The script sets up a MySQL server for the AirBnB project, creating a database, a new user, and granting specific privileges.

-- Create the hbnb_dev_db database if it doesn't exist
CREATE database IF NOT EXISTS hbnb_dev_db;

-- Create the hbnb_dev user if it doesn't exist and set the password to 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants the user  permisions
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
