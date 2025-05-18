CREATE DATABASE todo_db;

USE todo_db;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    deadline DATE,
    status ENUM("pending", "processing", "cancelled", "done") DEFAULT "pending"
    
);

