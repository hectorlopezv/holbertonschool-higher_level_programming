-- no comedy tonight
SELECT DISTINCT * FROM 
(
    SELECT tv_shows.title  
    FROM tv_show_genres  
    RIGHT JOIN tv_genres  
    ON tv_genres.id = tv_show_genres.genre_id  
    RIGHT JOIN tv_shows  ON tv_shows.id = tv_show_genres.show_id 
    WHERE tv_genres.name != 'Comedy' or tv_genres.name IS NULL
) AS SUBQUERY 
ORDER BY SUBQUERY.title;