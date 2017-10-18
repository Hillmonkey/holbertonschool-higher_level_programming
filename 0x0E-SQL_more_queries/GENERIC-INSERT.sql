-- push cities into some table
-- CLI syntax:
-- cat CITY-INSERT.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
INSERT INTO cities
	(id, state_id, city)
	VALUES
	(1,  1,  San Francisco),
	(2,  1,  San Jose),
	(4,  2,  Page),
	(6,  3,  Paris),
	(7,  3,  Houston),
	(8,  3,  Dallas);
