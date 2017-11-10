-- push cities into some table
-- CLI syntax:
-- cat CITIES-INSERT.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
INSERT INTO cities
	(state_id, name)
	VALUES
	(1,  'San Francisco'),
	(1,  'San Jose'),
	(2,  'Page'),
	(3,  'Paris'),
	(3,  'Houston'),
	(3,  'Dallas');
