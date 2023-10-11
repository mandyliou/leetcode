# Write your MySQL query statement below
SELECT ROUND(SUM(I.tiv_2016), 2) AS tiv_2016
FROM Insurance I
WHERE 
    I.tiv_2015 IN (
        SELECT tiv_2015
        FROM Insurance
        GROUP BY tiv_2015
        HAVING COUNT(*) > 1
    )
    AND NOT EXISTS (
        SELECT 1
        FROM Insurance
        WHERE lat = I.lat AND lon = I.lon AND pid != I.pid
    );
