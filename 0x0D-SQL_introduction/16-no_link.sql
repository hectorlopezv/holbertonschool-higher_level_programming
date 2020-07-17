-- say my name
SELECT score, name FROM second_table
HAVING name != 'NULL'
ORDER BY score DESC;