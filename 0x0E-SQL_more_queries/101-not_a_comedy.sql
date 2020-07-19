-- no comedy tonight
SELECT title 
FROM tv_shows
WHERE title NOT IN (


SELECT tv_shows.title
FROM tv_show_genres 
RIGHT JOIN tv_genres 
ON tv_genres.id = tv_show_genres.genre_id 
RIGHT JOIN tv_shows 
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy'
)
ORDER BY title;;