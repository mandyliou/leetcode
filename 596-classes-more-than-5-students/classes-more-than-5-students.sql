# Write your MySQL query statement below
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5; #filters out classes with less than 5 students