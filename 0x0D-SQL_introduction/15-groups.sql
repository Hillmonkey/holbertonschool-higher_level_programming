-- display scores, grouped by count, in descending order of 
SELECT score, COUNT(score) AS number
FROM
	second_table
GROUP BY
	score
ORDER BY
	COUNT(score) DESC;
