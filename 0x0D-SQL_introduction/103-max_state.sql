-- Display the max temperatues of each state ordered by State Name
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
