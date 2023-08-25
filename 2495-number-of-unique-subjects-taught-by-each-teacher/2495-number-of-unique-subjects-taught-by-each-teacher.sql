# Write your MySQL query statement below

SELECT teacher_id, 
        COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id #groups the rows based on teacher id's 
ORDER BY teacher_id #ascending order
