-- displays the top 3 of cities temperature during July and August
-- ordered by temperature (descending)
SELECT TOP 3 city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 8 AND MONTH = 7
GROUP BY city
ORDER BY avg_temp DESC;
