-- lists all records second_table except where name has no value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
