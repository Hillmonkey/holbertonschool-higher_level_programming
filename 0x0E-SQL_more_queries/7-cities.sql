-- create a database and within it, a table of states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
