-- Average temperature
SELECT city, AVG(value) AS avg_temp, month
FROM temperatures
WHERE month = 8 or month = 7
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
