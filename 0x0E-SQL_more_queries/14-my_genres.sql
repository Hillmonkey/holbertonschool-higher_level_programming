-- genres associated with the show Dexter
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_show.id
WHERE tv_show_genres.show_id =
	(SELECT id
	FROM tv_shows
	WHERE name = 'Dexter')
ORDER BY tv_genres.name
