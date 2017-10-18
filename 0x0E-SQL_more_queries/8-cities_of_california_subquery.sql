-- filter to cities in the state of California
SELECT id, state_id, state
	FROM cities
	ORDER BY id
	WHERE name = 'California';
