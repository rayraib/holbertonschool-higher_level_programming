-- Lists number of records with the same score in the table second_table
SELECT score, COUNT(score) number
FROM second_table
GROUP BY score
HAVING number > 0
ORDER BY number DESC;
