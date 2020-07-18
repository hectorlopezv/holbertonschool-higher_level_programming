-- creating states tables
CREATE DATABASE  IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS state(
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(256),
    PRIMARY KEY (id)
);