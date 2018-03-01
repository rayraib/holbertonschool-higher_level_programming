-- List all shows contained in the hbtn_0d_tvshows without a genre linked
SELECT title, genre_id
FROM tv_shows LEFT OUTER JOIN tv_show_genres
ON show_id = tv_shows.id 
WHERE genre_id IS NULL 
ORDER BY title ASC, genre_id ASC;
