-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT title, genre_id
FROM tv_show_genres INNER JOIN tv_shows
ON tv_shows.id = show_id
ORDER BY title ASC, genre_id ASC;
