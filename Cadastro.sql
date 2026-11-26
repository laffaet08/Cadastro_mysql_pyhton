CREATE DATABASE hortifruti;
USE hortifruti;

CREATE TABLE produto (
id INT auto_increment PRIMARY KEY,
nome VARCHAR (50) NOT NULL,
categoria VARCHAR (20) NOT NULL,
preco DECIMAL(7,2) NOT NULL 
);

-- 2 CRIAR O USUÁRIO 

CREATE USER 'app_hortifruti'@'localhost'
IDENTIFIED BY 'App@Horti2026';

GRANT SELECT, INSERT ON hortifruti.produto 
TO 'app_hortifruti'@'localhost';

SHOW GRANTS FOR 'app_hortifruti'@'localhost';

SELECT * FROM produto;	