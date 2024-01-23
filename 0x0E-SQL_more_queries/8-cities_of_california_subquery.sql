-- Script that lists all the cities of California in the database hbtn_0d_usa.
USE hbtn_0d_usa;

SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
