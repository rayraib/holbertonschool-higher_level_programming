-- Display the average temperatures by city ordered by temperatures
SELECT city, AVG(value)
FROM temperatures
GROUP BY city;
