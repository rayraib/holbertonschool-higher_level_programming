-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT title, genre_id
from tv_shows, tv_show_genres
WHERE tv_shows.id = show_id
ORDER BY title ASC, genre_id ASC;
