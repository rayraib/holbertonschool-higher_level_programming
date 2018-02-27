-- Display the average temperatures by city ordered by temperatures
SELECT city, AVG(value) AS avg_tmp
FROM temperatures
GROUP BY city;
