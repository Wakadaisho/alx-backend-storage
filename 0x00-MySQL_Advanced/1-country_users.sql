-- Create users table, with country enum column

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
    country enum('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
	PRIMARY KEY (id)
);
