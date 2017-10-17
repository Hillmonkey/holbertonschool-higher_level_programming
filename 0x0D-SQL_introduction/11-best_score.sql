-- select best scores
SELECT score, name
	FROM second_table
	WHERE id >= 10
	ORDER BY score DESC;
