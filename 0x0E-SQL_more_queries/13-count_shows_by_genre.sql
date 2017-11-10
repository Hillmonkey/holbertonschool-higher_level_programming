-- count number of shows associated with each genre
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) AS number_shows
	FROM tv_genres
	LEFT JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	GROUP BY
		tv_show_genres.show_id
	ORDER BY COUNT(tv_show_genres.show_id) DESC;
