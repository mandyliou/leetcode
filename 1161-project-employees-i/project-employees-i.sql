# Write your MySQL query statement below

SELECT p.project_id, ROUND(AVG(e.experience_years), 2) as average_years
FROM Project p 
JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id; #group resulting rows by project_id or would just avg all of the employees across all projects