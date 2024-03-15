CREATE DATABASE IF NOT EXISTS epicevents;

ALTER USER 'root'@'localhost' IDENTIFIED BY 'Toast13?';

DROP USER IF EXISTS 'root'@'localhost';

CREATE USER 'root'@'localhost' IDENTIFIED BY 'Toast13?';

GRANT ALL PRIVILEGES ON epicevents.* TO 'root'@'localhost';

FLUSH PRIVILEGES;

USE epicevents;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name_lastname VARCHAR(45),
    department ENUM('COM', 'GES', 'SUP'),
    password VARCHAR(45),
    email VARCHAR(45),
    token VARCHAR(300),
    secret_key VARCHAR(300)
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name_lastname VARCHAR(45),
    email VARCHAR(45),
    phone BIGINT,
    business_name VARCHAR(45),
    date_first_contact TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_date_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sales_contact INTEGER UNIQUE REFERENCES users(id)
);

CREATE TABLE contracts (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER UNIQUE REFERENCES customers(id),
    total_amount FLOAT DEFAULT 0,
    settled_amount FLOAT DEFAULT 0,
    remaining_amount FLOAT DEFAULT 0,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    contract_sign BOOLEAN DEFAULT FALSE
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    contract_id INTEGER UNIQUE REFERENCES contracts(id),
    title VARCHAR(45),
    date_hour_start TIMESTAMP,
    date_hour_end TIMESTAMP,
    address VARCHAR(45),
    guests INTEGER DEFAULT 0,
    notes TEXT,
    support_contact INTEGER REFERENCES users(id)
);

DELIMITER //

CREATE TRIGGER contracts_BEFORE_INSERT
BEFORE INSERT ON contracts
FOR EACH ROW
BEGIN
    SET NEW.remaining_amount = NEW.total_amount - NEW.settled_amount;
END//

CREATE TRIGGER contracts_BEFORE_UPDATE
BEFORE UPDATE ON contracts
FOR EACH ROW
BEGIN
    SET NEW.remaining_amount = NEW.total_amount - NEW.settled_amount;
END//

DELIMITER ;
