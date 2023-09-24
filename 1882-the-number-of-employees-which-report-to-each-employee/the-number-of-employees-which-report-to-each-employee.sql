# Write your MySQL query statement below
SELECT 
    E.employee_id,
    E.name,
    COUNT(R.employee_id) AS reports_count,
    ROUND(AVG(R.age)) AS average_age
FROM Employees E
LEFT JOIN Employees R ON E.employee_id = R.reports_to
GROUP BY E.employee_id, E.name
HAVING COUNT(R.employee_id) > 0
ORDER BY E.employee_id;
