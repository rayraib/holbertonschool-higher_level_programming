-- List all genres of the show dexter
SELECT name
FROM tv_show_genres INNER JOIN tv_shows
ON show_id = tv_shows.id
INNER JOIN tv_genres 
ON tv_show_genres.genre_id = tv_genres.id
WHERE title = 'Dexter'
ORDER BY name ASC;
