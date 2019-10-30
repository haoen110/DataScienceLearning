CREATE DATABASE sdsc5003 CHARACTER SET utf8;

CREATE TABLE users(id INT(11) AUTO_INCREMENT PRIMARY KEY,
                   username VARCHAR(30),
                   email VARCHAR(100),
                   password VARCHAR(100),
                   register_date TIMESTAMP  DEFAULT CURRENT_TIMESTAMP);

