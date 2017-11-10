-- push states into some table
-- CLI syntax:
-- cat STATES-INSERT.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
INSERT INTO states
	(id, name)
VALUES
	(1,  'California'),
	(2,  'Arizona'),
	(3,  'Texas'),
	(4,  'Utah');
