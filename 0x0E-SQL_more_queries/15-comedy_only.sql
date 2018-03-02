-- Lists all Comedy shows in the database
SELECT title
FROM tv_show_genres INNER JOIN tv_genres
ON genre_id = tv_genres.id 
INNER JOIN tv_shows
ON show_id = tv_shows.id
WHERE name='Comedy'
ORDER BY title ASC;
