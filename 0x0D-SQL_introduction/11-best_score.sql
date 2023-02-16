-- lists all records of second_table with score >= 10
-- results should display both the score and the name (in this order)
-- records should be ordered by score in descending order
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
