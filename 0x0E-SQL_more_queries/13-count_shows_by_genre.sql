-- List all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- SELECT name, SUM(tv_genres.id) AS number_shows
SELECT name genre, COUNT(genre_id) AS number_shows
FROM tv_genres, tv_show_genres
WHERE id = genre_id
GROUP BY name
ORDER BY number_shows DESC;
