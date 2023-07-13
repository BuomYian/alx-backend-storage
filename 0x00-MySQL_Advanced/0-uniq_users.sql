-- Creates the "users" table.

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCAHR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
