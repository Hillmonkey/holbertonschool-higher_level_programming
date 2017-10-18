-- create a database and within it, a table of states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	FOREIGN KEY (state_id) REFERENCES states(state_id),
	name VARCHAR(256) NOT NULL
);
