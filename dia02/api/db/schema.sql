CREATE DATABASE IF NOT EXISTS company;

USE company;

CREATE TABLE IF NOT EXISTS employee(
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) DEFAULT NULL,
    salary INT(11) DEFAULT NULL,
    PRIMARY KEY(id)
);

INSERT INTO employee(name,salary)
VALUES 
('Marcel Lazo de la Vega',4000),
('Rocio Vizcarra',11000),
('Sandra Lazo de la Vega',21000),
('Marco Sosa',18000)
;

