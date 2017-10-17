-- this script lists names and scores without showing NULL names
select score, name
FROM
	second_table
WHERE
	name IS NOT NULL
ORDER BY
	score DESC;
