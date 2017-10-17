-- display scores, grouped by count, in descending order of 
SELECT score, count(number) AS number
GROUP BY
	score
ORDER BY
	count(number) DESC;
