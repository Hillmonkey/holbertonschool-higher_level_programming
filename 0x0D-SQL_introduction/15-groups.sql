-- number
SELECT score, count(*)
	AS score, "number"
GROUP BY
	score
ORDER BY
	score DESC;
